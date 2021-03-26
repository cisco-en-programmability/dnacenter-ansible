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
module: service_provider
short_description: Manage ServiceProvider objects of NetworkSettings
description:
- API to get service provider details (QoS).
- API to create service provider profile(QOS).
- API to update SP profile.
- API to delete Service Provider profile (QoS).
version_added: '1.0'
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

RETURN = """
get_service_provider_details:
    description: API to get service provider details (QoS).
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body (list of objects).
      returned: always
      type: list
      contains:
        instanceType:
          description: It is the service provider's instanceType.
          returned: always
          type: str
          sample: '<instancetype>'
        instanceUuid:
          description: It is the service provider's instanceUuid.
          returned: always
          type: str
          sample: '<instanceuuid>'
        namespace:
          description: It is the service provider's namespace.
          returned: always
          type: str
          sample: '<namespace>'
        type:
          description: It is the service provider's type.
          returned: always
          type: str
          sample: '<type>'
        key:
          description: It is the service provider's key.
          returned: always
          type: str
          sample: '<key>'
        version:
          description: It is the service provider's version.
          returned: always
          type: str
          sample: '1.0'
        value:
          description: It is the service provider's value.
          returned: always
          type: list
          contains:
            wanProvider:
              description: It is the service provider's wanProvider.
              returned: always
              type: str
              sample: '<wanprovider>'
            spProfileName:
              description: It is the service provider's spProfileName.
              returned: always
              type: str
              sample: '<spprofilename>'
            slaProfileName:
              description: It is the service provider's slaProfileName.
              returned: always
              type: str
              sample: '<slaprofilename>'

        groupUuid:
          description: It is the service provider's groupUuid.
          returned: always
          type: str
          sample: '<groupuuid>'
        inheritedGroupUuid:
          description: It is the service provider's inheritedGroupUuid.
          returned: always
          type: str
          sample: '<inheritedgroupuuid>'
        inheritedGroupName:
          description: It is the service provider's inheritedGroupName.
          returned: always
          type: str
          sample: '<inheritedgroupname>'

    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

create_sp_profile:
    description: API to create service provider profile(QOS).
    returned: success
    type: dict
    contains:
    executionId:
      description: Execution Id, property of the response body.
      returned: success
      type: str
      sample: '<executionid>'
    executionStatusUrl:
      description: Execution Status Url, property of the response body.
      returned: success
      type: str
      sample: '<executionstatusurl>'
    message:
      description: Message, property of the response body.
      returned: success
      type: str
      sample: '<message>'

update_sp_profile:
    description: API to update SP profile.
    returned: changed
    type: dict
    contains:
    executionId:
      description: Execution Id, property of the response body.
      returned: changed
      type: str
      sample: '<executionid>'
    executionStatusUrl:
      description: Execution Status Url, property of the response body.
      returned: changed
      type: str
      sample: '<executionstatusurl>'
    message:
      description: Message, property of the response body.
      returned: changed
      type: str
      sample: '<message>'

delete_sp_profile:
    description: API to delete Service Provider profile (QoS).
    returned: success
    type: dict
    contains:
    executionId:
      description: Execution Id, property of the response body.
      returned: success
      type: str
      sample: '<executionid>'
    executionStatusUrl:
      description: Execution Status Url, property of the response body.
      returned: success
      type: str
      sample: '<executionstatusurl>'
    message:
      description: Message, property of the response body.
      returned: success
      type: str
      sample: '<message>'

"""

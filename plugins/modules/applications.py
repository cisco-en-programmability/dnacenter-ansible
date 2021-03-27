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
module: applications
short_description: Manage Applications objects of ApplicationPolicy
description:
- Get Applications by offset/limit or by name.
- Delete existing application by its id.
- Create new Custom application.
- Edit the attributes of an existing application.
- Get the number of all existing Applications.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  limit:
    description:
    - The maximum number of Applications to be returned.
    type: int
  name:
    description:
    - Application's name.
    type: str
  offset:
    description:
    - The offset of the first application to be returned.
    type: int
  id:
    description:
    - Application's Id.
    - Required for state delete.
    type: str
  payload:
    description:
    - An object to send in the Request body.
    type: list
    required: True
    elements: dict
    suboptions:
      applicationSet:
        description:
        - It is the Applications's applicationSet.
        type: dict
        suboptions:
          idRef:
            description:
            - It is the Applications's idRef.
            type: str

      id:
        description:
        - It is the Applications's id.
        type: str
      name:
        description:
        - It is the Applications's name.
        type: str
      networkApplications:
        description:
        - It is the Applications's networkApplications.
        type: list
        elements: dict
        suboptions:
          appProtocol:
            description:
            - It is the Applications's appProtocol.
            type: str
          applicationSubType:
            description:
            - It is the Applications's applicationSubType.
            type: str
          applicationType:
            description:
            - It is the Applications's applicationType.
            type: str
          categoryId:
            description:
            - It is the Applications's categoryId.
            type: str
          displayName:
            description:
            - It is the Applications's displayName.
            type: str
          dscp:
            description:
            - It is the Applications's dscp.
            type: str
          engineId:
            description:
            - It is the Applications's engineId.
            type: str
          helpString:
            description:
            - It is the Applications's helpString.
            type: str
          id:
            description:
            - It is the Applications's id.
            type: str
          ignoreConflict:
            description:
            - It is the Applications's ignoreConflict.
            type: str
          longDescription:
            description:
            - It is the Applications's longDescription.
            type: str
          name:
            description:
            - It is the Applications's name.
            type: str
          popularity:
            description:
            - It is the Applications's popularity.
            type: str
          rank:
            description:
            - It is the Applications's rank.
            type: str
          serverName:
            description:
            - It is the Applications's serverName.
            type: str
          trafficClass:
            description:
            - It is the Applications's trafficClass.
            type: str
          url:
            description:
            - It is the Applications's url.
            type: str

      networkIdentity:
        description:
        - It is the Applications's networkIdentity.
        type: list
        elements: dict
        suboptions:
          displayName:
            description:
            - It is the Applications's displayName.
            type: str
          id:
            description:
            - It is the Applications's id.
            type: str
          lowerPort:
            description:
            - It is the Applications's lowerPort.
            type: str
          ports:
            description:
            - It is the Applications's ports.
            type: str
          protocol:
            description:
            - It is the Applications's protocol.
            type: str
          upperPort:
            description:
            - It is the Applications's upperPort.
            type: str


  count:
    description:
    - If true gets the number of objects.
    - Required for state query.
    type: bool

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.applications
# Reference by Internet resource
- name: Applications reference
  description: Complete reference of the Applications object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: Applications reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_applications
  cisco.dnac.applications:
    state: query  # required
    limit: 1  #  number
    name: SomeValue  # string
    offset: 1  #  number
  register: query_result
  
- name: delete_application
  cisco.dnac.applications:
    state: delete  # required
    id: SomeValue  # string, required
  
- name: create_application
  cisco.dnac.applications:
    state: create  # required
    payload:  # required
    - name: SomeValue  # string
      networkApplications:
      - appProtocol: SomeValue  # string
        applicationSubType: SomeValue  # string
        applicationType: SomeValue  # string
        categoryId: SomeValue  # string
        displayName: SomeValue  # string
        engineId: SomeValue  # string
        helpString: SomeValue  # string
        longDescription: SomeValue  # string
        name: SomeValue  # string
        popularity: SomeValue  # string
        rank: SomeValue  # string
        trafficClass: SomeValue  # string
        serverName: SomeValue  # string
        url: SomeValue  # string
        dscp: SomeValue  # string
        ignoreConflict: SomeValue  # string
      networkIdentity:
      - displayName: SomeValue  # string
        lowerPort: SomeValue  # string
        ports: SomeValue  # string
        protocol: SomeValue  # string
        upperPort: SomeValue  # string
      applicationSet:
        idRef: SomeValue  # string
  
- name: edit_application
  cisco.dnac.applications:
    state: update  # required
    payload:  # required
    - id: SomeValue  # string
      name: SomeValue  # string
      networkApplications:
      - id: SomeValue  # string
        appProtocol: SomeValue  # string
        applicationSubType: SomeValue  # string
        applicationType: SomeValue  # string
        categoryId: SomeValue  # string
        displayName: SomeValue  # string
        engineId: SomeValue  # string
        helpString: SomeValue  # string
        longDescription: SomeValue  # string
        name: SomeValue  # string
        popularity: SomeValue  # string
        rank: SomeValue  # string
        trafficClass: SomeValue  # string
        serverName: SomeValue  # string
        url: SomeValue  # string
        dscp: SomeValue  # string
        ignoreConflict: SomeValue  # string
      networkIdentity:
      - id: SomeValue  # string
        displayName: SomeValue  # string
        lowerPort: SomeValue  # string
        ports: SomeValue  # string
        protocol: SomeValue  # string
        upperPort: SomeValue  # string
      applicationSet:
        idRef: SomeValue  # string
  
- name: get_applications_count
  cisco.dnac.applications:
    state: query  # required
    count: True  # boolean, required
  register: query_result
  
"""

RETURN = """
get_applications:
    description: Get Applications by offset/limit or by name.
    returned: always
    type: dict
    contains:
    payload:
      description: It is the Applications's payload.
      returned: always
      type: list
      contains:
        id:
          description: It is the Applications's id.
          returned: always
          type: str
          sample: '478012'
        name:
          description: It is the Applications's name.
          returned: always
          type: str
          sample: '<name>'
        networkApplications:
          description: It is the Applications's networkApplications.
          returned: always
          type: list
          contains:
            id:
              description: It is the Applications's id.
              returned: always
              type: str
              sample: '478012'
            appProtocol:
              description: It is the Applications's appProtocol.
              returned: always
              type: str
              sample: '<appprotocol>'
            applicationSubType:
              description: It is the Applications's applicationSubType.
              returned: always
              type: str
              sample: '<applicationsubtype>'
            applicationType:
              description: It is the Applications's applicationType.
              returned: always
              type: str
              sample: '<applicationtype>'
            categoryId:
              description: It is the Applications's categoryId.
              returned: always
              type: str
              sample: '<categoryid>'
            displayName:
              description: It is the Applications's displayName.
              returned: always
              type: str
              sample: '<displayname>'
            engineId:
              description: It is the Applications's engineId.
              returned: always
              type: str
              sample: '<engineid>'
            helpString:
              description: It is the Applications's helpString.
              returned: always
              type: str
              sample: '<helpstring>'
            longDescription:
              description: It is the Applications's longDescription.
              returned: always
              type: str
              sample: '<longdescription>'
            name:
              description: It is the Applications's name.
              returned: always
              type: str
              sample: '<name>'
            popularity:
              description: It is the Applications's popularity.
              returned: always
              type: str
              sample: '<popularity>'
            rank:
              description: It is the Applications's rank.
              returned: always
              type: str
              sample: '<rank>'
            trafficClass:
              description: It is the Applications's trafficClass.
              returned: always
              type: str
              sample: '<trafficclass>'
            serverName:
              description: It is the Applications's serverName.
              returned: always
              type: str
              sample: '<servername>'
            url:
              description: It is the Applications's url.
              returned: always
              type: str
              sample: '<url>'
            dscp:
              description: It is the Applications's dscp.
              returned: always
              type: str
              sample: '<dscp>'
            ignoreConflict:
              description: It is the Applications's ignoreConflict.
              returned: always
              type: str
              sample: '<ignoreconflict>'

        networkIdentity:
          description: It is the Applications's networkIdentity.
          returned: always
          type: list
          contains:
            id:
              description: It is the Applications's id.
              returned: always
              type: str
              sample: '478012'
            displayName:
              description: It is the Applications's displayName.
              returned: always
              type: str
              sample: '<displayname>'
            lowerPort:
              description: It is the Applications's lowerPort.
              returned: always
              type: str
              sample: '<lowerport>'
            ports:
              description: It is the Applications's ports.
              returned: always
              type: str
              sample: '<ports>'
            protocol:
              description: It is the Applications's protocol.
              returned: always
              type: str
              sample: '<protocol>'
            upperPort:
              description: It is the Applications's upperPort.
              returned: always
              type: str
              sample: '<upperport>'

        applicationSet:
          description: It is the Applications's applicationSet.
          returned: always
          type: dict
          contains:
            idRef:
              description: It is the Applications's idRef.
              returned: always
              type: str
              sample: '<idref>'



delete_application:
    description: Delete existing application by its id.
    returned: success
    type: dict
    contains:
    response:
      description: Response, property of the response body.
      returned: success
      type: dict
      contains:
        taskId:
          description: It is the Applications's taskId.
          returned: success
          type: str
          sample: 'aeed229047801200e0ef563dbb9a71c2'
        url:
          description: It is the Applications's url.
          returned: success
          type: str
          sample: '<url>'

    version:
      description: Version, property of the response body.
      returned: success
      type: str
      sample: '1.0'

create_application:
    description: Create new Custom application.
    returned: success
    type: dict
    contains:
    response:
      description: Response, property of the response body.
      returned: success
      type: dict
      contains:
        taskId:
          description: It is the Applications's taskId.
          returned: success
          type: str
          sample: 'aeed229047801200e0ef563dbb9a71c2'
        url:
          description: It is the Applications's url.
          returned: success
          type: str
          sample: '<url>'

    version:
      description: Version, property of the response body.
      returned: success
      type: str
      sample: '1.0'

edit_application:
    description: Edit the attributes of an existing application.
    returned: changed
    type: dict
    contains:
    response:
      description: Response, property of the response body.
      returned: changed
      type: dict
      contains:
        taskId:
          description: It is the Applications's taskId.
          returned: changed
          type: str
          sample: 'aeed229047801200e0ef563dbb9a71c2'
        url:
          description: It is the Applications's url.
          returned: changed
          type: str
          sample: '<url>'

    version:
      description: Version, property of the response body.
      returned: changed
      type: str
      sample: '1.0'

get_applications_count:
    description: Get the number of all existing Applications.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body.
      returned: always
      type: str
      sample: '<response>'
    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

"""

#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

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
  register: nm_get_applications

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
  register: nm_get_applications_count

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
  sample: application_policy.create_application
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: list
  sample:
"""

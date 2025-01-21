#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: applications
short_description: Resource module for Applications
description:
- This module represents an alias of the module applications_v1
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id query parameter. Application's Id.
    type: str
  payload:
    description: Applications's payload.
    elements: dict
    suboptions:
      applicationSet:
        description: Applications's applicationSet.
        suboptions:
          idRef:
            description: Id Ref.
            type: str
        type: dict
      name:
        description: Name.
        type: str
      networkApplications:
        description: Applications's networkApplications.
        elements: dict
        suboptions:
          appProtocol:
            description: App Protocol.
            type: str
          applicationSubType:
            description: Application Sub Type.
            type: str
          applicationType:
            description: Application Type.
            type: str
          categoryId:
            description: Category Id.
            type: str
          displayName:
            description: Display Name.
            type: str
          dscp:
            description: Dscp.
            type: str
          engineId:
            description: Engine Id.
            type: str
          helpString:
            description: Help String.
            type: str
          ignoreConflict:
            description: Ignore Conflict.
            type: str
          longDescription:
            description: Long Description.
            type: str
          name:
            description: Name.
            type: str
          popularity:
            description: Popularity.
            type: str
          rank:
            description: Rank.
            type: str
          serverName:
            description: Server Name.
            type: str
          trafficClass:
            description: Traffic Class.
            type: str
          url:
            description: Url.
            type: str
        type: list
      networkIdentity:
        description: Applications's networkIdentity.
        elements: dict
        suboptions:
          displayName:
            description: Display Name.
            type: str
          lowerPort:
            description: Lower Port.
            type: str
          ports:
            description: Ports.
            type: str
          protocol:
            description: Protocol.
            type: str
          upperPort:
            description: Upper Port.
            type: str
        type: list
    type: list
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Application Policy CreateApplicationV1
  description: Complete reference of the CreateApplicationV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!create-application
- name: Cisco DNA Center documentation for Application Policy DeleteApplicationV1
  description: Complete reference of the DeleteApplicationV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!delete-application
- name: Cisco DNA Center documentation for Application Policy EditApplicationV1
  description: Complete reference of the EditApplicationV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!edit-application
notes:
  - SDK Method used are
    application_policy.ApplicationPolicy.create_application_v1,
    application_policy.ApplicationPolicy.delete_application_v1,
    application_policy.ApplicationPolicy.edit_application_v1,

  - Paths used are
    post /dna/intent/api/v1/applications,
    delete /dna/intent/api/v1/applications,
    put /dna/intent/api/v1/applications,
  - It should be noted that this module is an alias of applications_v1

"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.applications:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    payload:
    - applicationSet:
        idRef: string
      name: string
      networkApplications:
      - appProtocol: string
        applicationSubType: string
        applicationType: string
        categoryId: string
        displayName: string
        dscp: string
        engineId: string
        helpString: string
        ignoreConflict: string
        longDescription: string
        name: string
        popularity: string
        rank: string
        serverName: string
        trafficClass: string
        url: string
      networkIdentity:
      - displayName: string
        lowerPort: string
        ports: string
        protocol: string
        upperPort: string

- name: Update all
  cisco.dnac.applications:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    payload:
    - applicationSet:
        idRef: string
      id: string
      name: string
      networkApplications:
      - appProtocol: string
        applicationSubType: string
        applicationType: string
        categoryId: string
        displayName: string
        dscp: string
        engineId: string
        helpString: string
        id: string
        ignoreConflict: string
        longDescription: string
        name: string
        popularity: string
        rank: string
        serverName: string
        trafficClass: string
        url: string
      networkIdentity:
      - displayName: string
        id: string
        lowerPort: string
        ports: string
        protocol: string
        upperPort: string

- name: Delete all
  cisco.dnac.applications:
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

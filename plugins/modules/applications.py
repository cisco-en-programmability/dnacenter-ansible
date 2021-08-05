#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: applications
short_description: Resource module for Applications
description:
- Manage operations create, update and delete of the resource Applications.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  id:
    description: Id query parameter. Application's Id.
    type: str
  payload:
    description: Applications's payload.
    suboptions:
      applicationSet:
        description: Applications's applicationSet.
        suboptions:
          idRef:
            description: Applications's idRef.
            type: str
        type: dict
      id:
        description: Applications's id.
        type: str
      name:
        description: Applications's name.
        type: str
      networkApplications:
        description: Applications's networkApplications.
        suboptions:
          appProtocol:
            description: Applications's appProtocol.
            type: str
          applicationSubType:
            description: Applications's applicationSubType.
            type: str
          applicationType:
            description: Applications's applicationType.
            type: str
          categoryId:
            description: Applications's categoryId.
            type: str
          displayName:
            description: Applications's displayName.
            type: str
          dscp:
            description: Applications's dscp.
            type: str
          engineId:
            description: Applications's engineId.
            type: str
          helpString:
            description: Applications's helpString.
            type: str
          id:
            description: Applications's id.
            type: str
          ignoreConflict:
            description: Applications's ignoreConflict.
            type: str
          longDescription:
            description: Applications's longDescription.
            type: str
          name:
            description: Applications's name.
            type: str
          popularity:
            description: Applications's popularity.
            type: str
          rank:
            description: Applications's rank.
            type: str
          serverName:
            description: Applications's serverName.
            type: str
          trafficClass:
            description: Applications's trafficClass.
            type: str
          url:
            description: Applications's url.
            type: str
        type: list
      networkIdentity:
        description: Applications's networkIdentity.
        suboptions:
          displayName:
            description: Applications's displayName.
            type: str
          id:
            description: Applications's id.
            type: str
          lowerPort:
            description: Applications's lowerPort.
            type: str
          ports:
            description: Applications's ports.
            type: str
          protocol:
            description: Applications's protocol.
            type: str
          upperPort:
            description: Applications's upperPort.
            type: str
        type: list
    type: list
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Applications reference
  description: Complete reference of the Applications object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
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

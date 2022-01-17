#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: tag
short_description: Resource module for Tag
description:
- Manage operations create, update and delete of the resource Tag.
- Updates a tag specified by id.
- Creates tag with specified tag attributes.
- Deletes a tag specified by id.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  description:
    description: Tag's description.
    type: str
  dynamicRules:
    description: Tag's dynamicRules.
    suboptions:
      memberType:
        description: Tag's memberType.
        type: str
      rules:
        description: Tag's rules.
        suboptions:
          items:
            description: Tag's items.
            elements: dict
            type: list
          name:
            description: Tag's name.
            type: str
          operation:
            description: Tag's operation.
            type: str
          value:
            description: Tag's value.
            type: str
          values:
            description: Tag's values.
            elements: str
            type: list
        type: dict
    type: list
  id:
    description: Tag's id.
    type: str
  instanceTenantId:
    description: Tag's instanceTenantId.
    type: str
  name:
    description: Tag's name.
    type: str
  systemTag:
    description: SystemTag flag.
    type: bool
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference to SDK documentation of current version
- name: SDK function update_tag used
  link: >
    https://dnacentersdk.rtfd.io/en/latest/api/api.html#dnacentersdk.api.v2_2_3_3.
    tag.Tag.update_tag

- name: SDK function delete_tag used
  link: >
    https://dnacentersdk.rtfd.io/en/latest/api/api.html#dnacentersdk.api.v2_2_3_3.
    tag.Tag.delete_tag

- name: SDK function create_tag used
  link: >
    https://dnacentersdk.rtfd.io/en/latest/api/api.html#dnacentersdk.api.v2_2_3_3.
    tag.Tag.create_tag

notes:
  - Paths used are put /dna/intent/api/v1/tag,
    post /dna/intent/api/v1/tag,
    delete /dna/intent/api/v1/tag/{id}
"""

EXAMPLES = r"""
- name: Update all
  cisco.dnac.tag:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    description: string
    dynamicRules:
    - memberType: string
      rules:
        items:
        - {}
        name: string
        operation: string
        value: string
        values:
        - string
    id: string
    instanceTenantId: string
    name: string
    systemTag: true

- name: Create
  cisco.dnac.tag:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    description: string
    dynamicRules:
    - memberType: string
      rules:
        items:
        - {}
        name: string
        operation: string
        value: string
        values:
        - string
    id: string
    instanceTenantId: string
    name: string
    systemTag: true

- name: Delete by id
  cisco.dnac.tag:
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
      "version": "string",
      "response": {
        "taskId": "string",
        "url": "string"
      }
    }
"""

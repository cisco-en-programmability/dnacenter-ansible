#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: service_provider_update
short_description: Resource module for Service Provider Update
description:
- Manage operation update of the resource Service Provider Update.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  settings:
    description: Service Provider Update's settings.
    suboptions:
      qos:
        description: Service Provider Update's qos.
        suboptions:
          model:
            description: Service Provider Update's model.
            type: str
          oldProfileName:
            description: Service Provider Update's oldProfileName.
            type: str
          profileName:
            description: Service Provider Update's profileName.
            type: str
          wanProvider:
            description: Service Provider Update's wanProvider.
            type: str
        type: list
    type: dict
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Service Provider Update reference
  description: Complete reference of the Service Provider Update object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Update all
  cisco.dnac.service_provider_update:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    settings:
      qos:
      - model: string
        oldProfileName: string
        profileName: string
        wanProvider: string

- name: Create
  cisco.dnac.service_provider_update:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    settings:
      qos:
      - model: string
        profileName: string
        wanProvider: string

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "executionId": "string",
      "executionStatusUrl": "string",
      "message": "string"
    }
"""

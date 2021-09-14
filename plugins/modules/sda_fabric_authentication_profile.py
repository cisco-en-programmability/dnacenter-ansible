#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_fabric_authentication_profile
short_description: Resource module for Sda Fabric Authentication Profile
description:
- Manage operations create, update and delete of the resource Sda Fabric Authentication Profile.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  payload:
    description: Sda Fabric Authentication Profile's payload.
    suboptions:
      authenticateTemplateName:
        description: Authenticate Template Name.
        type: str
      siteNameHierarchy:
        description: Site Name Hierarchy.
        type: str
    type: list
  siteNameHierarchy:
    description: SiteNameHierarchy query parameter.
    type: str
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Sda Fabric Authentication Profile reference
  description: Complete reference of the Sda Fabric Authentication Profile object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.sda_fabric_authentication_profile:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    payload:
    - siteNameHierarchy: string
      authenticateTemplateName: string

- name: Update all
  cisco.dnac.sda_fabric_authentication_profile:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    payload:
    - siteNameHierarchy: string
      authenticateTemplateName: string

- name: Delete all
  cisco.dnac.sda_fabric_authentication_profile:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    siteNameHierarchy: string

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "status": "string",
      "description": "string",
      "executionStatusUrl": "string"
    }
"""

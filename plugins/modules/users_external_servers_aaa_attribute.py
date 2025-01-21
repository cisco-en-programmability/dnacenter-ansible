#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: users_external_servers_aaa_attribute
short_description: Resource module for Users External Servers Aaa Attribute
description:
- This module represents an alias of the module users_external_servers_aaa_attribute_v1
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  attributeName:
    description: Name of the custom AAA attribute.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for User and Roles AddAndUpdateAAAAttributeAPIV1
  description: Complete reference of the AddAndUpdateAAAAttributeAPIV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!add-and-update-aaa-attribute-api
- name: Cisco DNA Center documentation for User and Roles DeleteAAAAttributeAPIV1
  description: Complete reference of the DeleteAAAAttributeAPIV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!delete-aaa-attribute-api
notes:
  - SDK Method used are
    user_and_roles.UserandRoles.add_and_update_aaa_attribute_api_v1,
    user_and_roles.UserandRoles.delete_aaa_attribute_api_v1,

  - Paths used are
    post /dna/system/api/v1/users/external-servers/aaa-attribute,
    delete /dna/system/api/v1/users/external-servers/aaa-attribute,
  - It should be noted that this module is an alias of users_external_servers_aaa_attribute_v1

"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.users_external_servers_aaa_attribute:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    attributeName: string

- name: Delete all
  cisco.dnac.users_external_servers_aaa_attribute:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent

"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "message": "string"
    }
"""

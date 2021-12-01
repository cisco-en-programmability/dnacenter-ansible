#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: service_provider_info
short_description: Information module for Service Provider
description:
- Get all Service Provider.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Service Provider reference
  description: Complete reference of the Service Provider object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Service Provider
  cisco.dnac.service_provider_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "instanceType": "string",
          "instanceUuid": "string",
          "namespace": "string",
          "type": "string",
          "key": "string",
          "version": "string",
          "value": [
            {
              "wanProvider": "string",
              "spProfileName": "string",
              "slaProfileName": "string"
            }
          ],
          "groupUuid": "string",
          "inheritedGroupUuid": "string",
          "inheritedGroupName": "string"
        }
      ],
      "version": "string"
    }
"""

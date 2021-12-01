#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_provision_ssid_delete_reprovision
short_description: Resource module for Wireless Provision Ssid Delete Reprovision
description:
- Manage operation delete of the resource Wireless Provision Ssid Delete Reprovision.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  managedAPLocations:
    description: ManagedAPLocations path parameter.
    type: str
  ssidName:
    description: SsidName path parameter.
    type: str
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Wireless Provision Ssid Delete Reprovision reference
  description: Complete reference of the Wireless Provision Ssid Delete Reprovision object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Delete by id
  cisco.dnac.wireless_provision_ssid_delete_reprovision:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    managedAPLocations: string
    ssidName: string

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

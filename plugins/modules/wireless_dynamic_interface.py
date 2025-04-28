#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: wireless_dynamic_interface
short_description: Resource module for Wireless Dynamic Interface
description:
  - This module represents an alias of the module wireless_dynamic_interface_v1
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  interfaceName:
    description: InterfaceName query parameter. Valid interface-name to be deleted.
    type: str
  vlanId:
    description: Vlan Id.
    type: float
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Wireless CreateUpdateDynamicInterfaceV1
    description: Complete reference of the CreateUpdateDynamicInterfaceV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!create-update-dynamic-interface
  - name: Cisco DNA Center documentation for Wireless DeleteDynamicInterfaceV1
    description: Complete reference of the DeleteDynamicInterfaceV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-dynamic-interface
notes:
  - SDK Method used are wireless.Wireless.create_update_dynamic_interface_v1, wireless.Wireless.delete_dynamic_interface_v1,
  - Paths used are post /dna/intent/api/v1/wireless/dynamic-interface, delete /dna/intent/api/v1/wireless/dynamic-interface,
  - It should be noted that this module is an alias of wireless_dynamic_interface_v1
"""
EXAMPLES = r"""
- name: Delete all
  cisco.dnac.wireless_dynamic_interface:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    headers: '{{my_headers | from_json}}'
    interfaceName: string
- name: Create
  cisco.dnac.wireless_dynamic_interface:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    interfaceName: string
    vlanId: 0
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

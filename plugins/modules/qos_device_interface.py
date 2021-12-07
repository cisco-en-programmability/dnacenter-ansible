#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: qos_device_interface
short_description: Resource module for Qos Device Interface
description:
- Manage operations create, update and delete of the resource Qos Device Interface.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter. Id of the qos device info, this object holds all
      qos device interface infos associate with network device id.
    type: str
  payload:
    description: Qos Device Interface's payload.
    suboptions:
      excludedInterfaces:
        description: Excluded interfaces ids.
        elements: str
        type: list
      id:
        description: Id of Qos device info.
        type: str
      name:
        description: Device name.
        type: str
      networkDeviceId:
        description: Network device id.
        type: str
      qosDeviceInterfaceInfo:
        description: Qos Device Interface's qosDeviceInterfaceInfo.
        suboptions:
          dmvpnRemoteSitesBw:
            description: Dmvpn remote sites bandwidth.
            elements: int
            type: list
          instanceId:
            description: Instance id.
            type: int
          interfaceId:
            description: Interface id.
            type: str
          interfaceName:
            description: Interface name.
            type: str
          label:
            description: SP Profile name.
            type: str
          role:
            description: Interface role.
            type: str
          uploadBW:
            description: Upload bandwidth.
            type: int
        type: list
    type: list
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Qos Device Interface reference
  description: Complete reference of the Qos Device Interface object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Update all
  cisco.dnac.qos_device_interface:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present

- name: Create
  cisco.dnac.qos_device_interface:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present

- name: Delete by id
  cisco.dnac.qos_device_interface:
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

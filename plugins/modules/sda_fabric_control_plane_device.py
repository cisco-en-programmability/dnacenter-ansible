#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_fabric_control_plane_device
short_description: Resource module for Sda Fabric Control Plane Device
description:
- Manage operations create and delete of the resource Sda Fabric Control Plane Device.
- Add control plane device in SDA Fabric.
- Delete control plane device in SDA Fabric.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  deviceManagementIpAddress:
    version_added: "4.0.0"
    description: DeviceManagementIpAddress query parameter.
    type: str
  siteNameHierarchy:
    version_added: "4.0.0"
    description: Site Name Hierarchy of provisioned Device(site should be fabric site).
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
notes:
  - SDK Method used are
    sda.Sda.add_control_plane_device,
    sda.Sda.delete_control_plane_device,

  - Paths used are
    post /dna/intent/api/v1/business/sda/control-plane-device,
    delete /dna/intent/api/v1/business/sda/control-plane-device,

"""

EXAMPLES = r"""
- name: Delete all
  cisco.dnac.sda_fabric_control_plane_device:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    deviceManagementIpAddress: string

- name: Create
  cisco.dnac.sda_fabric_control_plane_device:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    deviceManagementIpAddress: string
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
      "taskId": "string",
      "taskStatusUrl": "string",
      "executionStatusUrl": "string",
      "executionId": "string"
    }
"""

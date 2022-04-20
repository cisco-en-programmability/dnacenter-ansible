#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_port_assignment_for_access_point
short_description: Resource module for Sda Port Assignment For Access Point
description:
- Manage operations create and delete of the resource Sda Port Assignment For Access Point.
- Add Port assignment for access point in SDA Fabric.
- Delete Port assignment for access point in SDA Fabric.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  authenticateTemplateName:
    version_added: "4.0.0"
    description: Authenticate TemplateName associated to siteNameHierarchy.
    type: str
  dataIpAddressPoolName:
    version_added: "4.0.0"
    description: Ip Pool Name, that is assigned to INFRA_VN.
    type: str
  deviceManagementIpAddress:
    version_added: "4.0.0"
    description: Management Ip Address of the edge device.
    type: str
  interfaceDescription:
    version_added: "4.0.0"
    description: Details or note of interface assignment.
    type: str
  interfaceName:
    description: Interface Name of the edge device.
    type: str
  siteNameHierarchy:
    version_added: "4.0.0"
    description: Site Name Hierarchy should be a valid fabric site name hierarchy. E.g
      Global/USA/San Jose.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
notes:
  - SDK Method used are
    sda.Sda.add_port_assignment_for_access_point,
    sda.Sda.delete_port_assignment_for_access_point,

  - Paths used are
    post /dna/intent/api/v1/business/sda/hostonboarding/access-point,
    delete /dna/intent/api/v1/business/sda/hostonboarding/access-point,

"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.sda_port_assignment_for_access_point:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    authenticateTemplateName: string
    dataIpAddressPoolName: string
    deviceManagementIpAddress: string
    interfaceDescription: string
    interfaceName: string
    siteNameHierarchy: string

- name: Delete all
  cisco.dnac.sda_port_assignment_for_access_point:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    deviceManagementIpAddress: string
    interfaceName: string

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

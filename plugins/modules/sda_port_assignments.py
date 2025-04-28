#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: sda_port_assignments
short_description: Resource module for Sda Port Assignments
description:
  - This module represents an alias of the module sda_port_assignments_v1
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  dataVlanName:
    description: DataVlanName query parameter. Data VLAN name of the port assignment.
    type: str
  fabricId:
    description: FabricId query parameter. ID of the fabric the device is assigned
      to.
    type: str
  id:
    description: Id path parameter. ID of the port assignment.
    type: str
  interfaceName:
    description: InterfaceName query parameter. Interface name of the port assignment.
    type: str
  networkDeviceId:
    description: NetworkDeviceId query parameter. Network device ID of the port assignment.
    type: str
  payload:
    description: Sda Port Assignments's payload.
    elements: dict
    suboptions:
      authenticateTemplateName:
        description: Authenticate template name of the port assignment.
        type: str
      connectedDeviceType:
        description: Connected device type of the port assignment.
        type: str
      dataVlanName:
        description: Data VLAN name of the port assignment.
        type: str
      fabricId:
        description: ID of the fabric the device is assigned to.
        type: str
      interfaceDescription:
        description: Interface description of the port assignment.
        type: str
      interfaceName:
        description: Interface name of the port assignment.
        type: str
      networkDeviceId:
        description: Network device ID of the port assignment.
        type: str
      securityGroupName:
        description: Security group name of the port assignment.
        type: str
      voiceVlanName:
        description: Voice VLAN name of the port assignment.
        type: str
    type: list
  voiceVlanName:
    description: VoiceVlanName query parameter. Voice VLAN name of the port assignment.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for SDA AddPortAssignmentsV1
    description: Complete reference of the AddPortAssignmentsV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!add-port-assignments
  - name: Cisco DNA Center documentation for SDA DeletePortAssignmentByIdV1
    description: Complete reference of the DeletePortAssignmentByIdV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-port-assignment-by-id
  - name: Cisco DNA Center documentation for SDA DeletePortAssignmentsV1
    description: Complete reference of the DeletePortAssignmentsV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-port-assignments
  - name: Cisco DNA Center documentation for SDA UpdatePortAssignmentsV1
    description: Complete reference of the UpdatePortAssignmentsV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!update-port-assignments
notes:
  - SDK Method used are sda.Sda.add_port_assignments_v1, sda.Sda.delete_port_assignment_by_id_v1,
    sda.Sda.update_port_assignments_v1,
  - Paths used are post /dna/intent/api/v1/sda/portAssignments, delete /dna/intent/api/v1/sda/portAssignments,
    delete /dna/intent/api/v1/sda/portAssignments/{id}, put /dna/intent/api/v1/sda/portAssignments,
  - It should be noted that this module is an alias of sda_port_assignments_v1
"""
EXAMPLES = r"""
- name: Create
  cisco.dnac.sda_port_assignments:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    payload:
      - authenticateTemplateName: string
        connectedDeviceType: string
        dataVlanName: string
        fabricId: string
        interfaceDescription: string
        interfaceName: string
        networkDeviceId: string
        securityGroupName: string
        voiceVlanName: string
- name: Update all
  cisco.dnac.sda_port_assignments:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    payload:
      - authenticateTemplateName: string
        connectedDeviceType: string
        dataVlanName: string
        fabricId: string
        id: string
        interfaceDescription: string
        interfaceName: string
        networkDeviceId: string
        scalableGroupName: string
        voiceVlanName: string
- name: Delete all
  cisco.dnac.sda_port_assignments:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    dataVlanName: string
    fabricId: string
    interfaceName: string
    networkDeviceId: string
    voiceVlanName: string
- name: Delete by id
  cisco.dnac.sda_port_assignments:
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

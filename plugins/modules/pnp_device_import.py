#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: pnp_device_import
short_description: Resource module for Pnp Device Import
description:
- This module represents an alias of the module pnp_device_import_v1
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  payload:
    description: Pnp Device Import's payload.
    elements: dict
    suboptions:
      _id:
        description: Id.
        type: str
      deviceInfo:
        description: Pnp Device Import's deviceInfo.
        suboptions:
          description:
            description: Description.
            type: str
          deviceSudiSerialNos:
            description: Device Sudi Serial Nos.
            elements: str
            type: list
          hostname:
            description: Hostname.
            type: str
          macAddress:
            description: Mac Address.
            type: str
          pid:
            description: Pid.
            type: str
          serialNumber:
            description: Serial Number.
            type: str
          siteId:
            description: Site Id.
            type: str
          stack:
            description: Stack.
            type: bool
          stackInfo:
            description: Pnp Device Import's stackInfo.
            suboptions:
              isFullRing:
                description: Is Full Ring.
                type: bool
              stackMemberList:
                description: Pnp Device Import's stackMemberList.
                elements: dict
                suboptions:
                  hardwareVersion:
                    description: Hardware Version.
                    type: str
                  licenseLevel:
                    description: License Level.
                    type: str
                  licenseType:
                    description: License Type.
                    type: str
                  macAddress:
                    description: Mac Address.
                    type: str
                  pid:
                    description: Pid.
                    type: str
                  priority:
                    description: Priority.
                    type: float
                  role:
                    description: Role.
                    type: str
                  serialNumber:
                    description: Serial Number.
                    type: str
                  softwareVersion:
                    description: Software Version.
                    type: str
                  stackNumber:
                    description: Stack Number.
                    type: float
                  state:
                    description: State.
                    type: str
                  sudiSerialNumber:
                    description: Sudi Serial Number.
                    type: str
                type: list
              stackRingProtocol:
                description: Stack Ring Protocol.
                type: str
              supportsStackWorkflows:
                description: Supports Stack Workflows.
                type: bool
              totalMemberCount:
                description: Total Member Count.
                type: float
              validLicenseLevels:
                description: Valid License Levels.
                elements: str
                type: list
            type: dict
          sudiRequired:
            description: Is Sudi Required.
            type: bool
          userMicNumbers:
            description: User Mic Numbers.
            elements: str
            type: list
          userSudiSerialNos:
            description: User Sudi Serial Nos.
            elements: str
            type: list
          workflowId:
            description: Workflow Id.
            type: str
          workflowName:
            description: Workflow Name.
            type: str
        type: dict
    type: list
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Device Onboarding (PnP) ImportDevicesInBulkV1
  description: Complete reference of the ImportDevicesInBulkV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!import-devices-in-bulk-v-1
notes:
  - SDK Method used are
    device_onboarding_pnp.DeviceOnboardingPnp.import_devices_in_bulk_v1,

  - Paths used are
    post /dna/intent/api/v1/onboarding/pnp-device/import,
  - It should be noted that this module is an alias of pnp_device_import_v1

"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.pnp_device_import:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    payload:
    - _id: string
      deviceInfo:
        description: string
        deviceSudiSerialNos:
        - string
        hostname: string
        macAddress: string
        pid: string
        serialNumber: string
        siteId: string
        stack: true
        stackInfo:
          isFullRing: true
          stackMemberList:
          - hardwareVersion: string
            licenseLevel: string
            licenseType: string
            macAddress: string
            pid: string
            priority: 0
            role: string
            serialNumber: string
            softwareVersion: string
            stackNumber: 0
            state: string
            sudiSerialNumber: string
          stackRingProtocol: string
          supportsStackWorkflows: true
          totalMemberCount: 0
          validLicenseLevels:
          - string
        sudiRequired: true
        userMicNumbers:
        - string
        userSudiSerialNos:
        - string
        workflowId: string
        workflowName: string

"""
RETURN = r"""
dnac_response:
  This alias returns the output of pnp_device_import_v1.
"""

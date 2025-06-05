#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: sda_provision_device_v1
short_description: Resource module for Sda Provision Device V1
description:
  - Manage operations create, update and delete of the resource Sda Provision Device
    V1.
  - Provision Wired Device.
  - Delete provisioned Wired Device.
  - Re-Provision Wired Device.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  deviceManagementIpAddress:
    description: DeviceManagementIpAddress query parameter. Valid IP address of the
      device currently provisioned in a fabric site.
    type: str
  siteNameHierarchy:
    description: SiteNameHierarchy of the provisioned device.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for SDA ProvisionWiredDeviceV1
    description: Complete reference of the ProvisionWiredDeviceV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!provision-wired-device
  - name: Cisco DNA Center documentation for SDA DeleteProvisionedWiredDeviceV1
    description: Complete reference of the DeleteProvisionedWiredDeviceV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-provisioned-wired-device
  - name: Cisco DNA Center documentation for SDA ReProvisionWiredDeviceV1
    description: Complete reference of the ReProvisionWiredDeviceV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!re-provision-wired-device
notes:
  - SDK Method used are sda.Sda.delete_provisioned_wired_device_v1, sda.Sda.provision_wired_device_v1,
    sda.Sda.re_provision_wired_device_v1,
  - Paths used are post /dna/intent/api/v1/business/sda/provision-device, delete /dna/intent/api/v1/business/sda/provision-device,
    put /dna/intent/api/v1/business/sda/provision-device,
"""
EXAMPLES = r"""
- name: Delete all
  cisco.dnac.sda_provision_device_v1:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    deviceManagementIpAddress: string
- name: Update all
  cisco.dnac.sda_provision_device_v1:
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
- name: Create
  cisco.dnac.sda_provision_device_v1:
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

#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_provision_devices_v1
short_description: Resource module for Sda Provision Devices V1
description:
- Manage operations create, update and delete of the resource Sda Provision Devices V1.
- Provisions network devices to respective Sites based on user input.
- Delete provisioned devices based on query parameters.
- Deletes provisioned device based on Id.
- Re-provisions network devices to the site based on the user input.
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter. ID of the provisioned device.
    type: str
  networkDeviceId:
    description: NetworkDeviceId query parameter. ID of the network device.
    type: str
  payload:
    description: Sda Provision Devices's payload.
    elements: dict
    suboptions:
      networkDeviceId:
        description: ID of network device to be provisioned.
        type: str
      siteId:
        description: ID of the site this network device needs to be provisioned.
        type: str
    type: list
  siteId:
    description: SiteId query parameter. ID of the site hierarchy.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for SDA ProvisionDevicesV1
  description: Complete reference of the ProvisionDevicesV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!provision-devices-v-1
- name: Cisco DNA Center documentation for SDA DeleteProvisionedDeviceByIdV1
  description: Complete reference of the DeleteProvisionedDeviceByIdV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!delete-provisioned-device-by-id-v-1
- name: Cisco DNA Center documentation for SDA DeleteProvisionedDevicesV1
  description: Complete reference of the DeleteProvisionedDevicesV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!delete-provisioned-devices-v-1
- name: Cisco DNA Center documentation for SDA ReProvisionDevicesV1
  description: Complete reference of the ReProvisionDevicesV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!re-provision-devices-v-1
notes:
  - SDK Method used are
    sda.Sda.delete_provisioned_device_by_id_v1,
    sda.Sda.provision_devices_v1,
    sda.Sda.re_provision_devices_v1,

  - Paths used are
    post /dna/intent/api/v1/sda/provisionDevices,
    delete /dna/intent/api/v1/sda/provisionDevices,
    delete /dna/intent/api/v1/sda/provisionDevices/{id},
    put /dna/intent/api/v1/sda/provisionDevices,

"""

EXAMPLES = r"""
- name: Delete all
  cisco.dnac.sda_provision_devices_v1:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    networkDeviceId: string
    siteId: string

- name: Create
  cisco.dnac.sda_provision_devices_v1:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    payload:
    - networkDeviceId: string
      siteId: string

- name: Update all
  cisco.dnac.sda_provision_devices_v1:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    payload:
    - id: string
      networkDeviceId: string
      siteId: string

- name: Delete by id
  cisco.dnac.sda_provision_devices_v1:
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
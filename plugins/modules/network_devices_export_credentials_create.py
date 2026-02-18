#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_devices_export_credentials_create
short_description: Resource module for Network Devices Export Credentials Create
description:
  - Manage operation create of the resource Network Devices Export Credentials Create. - > Exports device credentials of all
    network devices in the inventory to an encrypted CSV file. To export credentials for selected devices only, provide the
    networkDeviceIds parameter in the request body. The exported file will be in zip format encrypted using the password provided
    in the request body. The ZIP file will contain a CSV file with the credentials of the selected network devices. If networkDeviceIds
    is not provided, then the credentials of all the network devices will be exported. Credentials for access points and Meraki
    devices cannot be exported. The response contains a task ID. Use the /dna/intent/api/v1/tasks/{taskId} API to check the
    status of the task. The task will be completed when the file is ready for download. The download URL will be available
    in the resultLocation attribute of the task API response.
version_added: '6.46.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  exportSshKey:
    description: Flag to export the SSH key. If not provided, the SSH key will not be exported.
    type: bool
  networkDeviceIds:
    description: List of network device IDs to export the credentials for. If not provided, all devices will be exported.
    elements: str
    type: list
  password:
    description: Password to encrypt the CSV file. A password must contain, at minimum 8 characters, one lowercase letter,
      one uppercase letter, one number, one special character (-=;,./~!@#$%^&*()_+{}| ?). The password cannot contain spaces
      or the characters < >.
    type: str
requirements:
  - dnacentersdk >= 2.11.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Devices ExportsTheCredentialsOfNetworkDevices
    description: Complete reference of the ExportsTheCredentialsOfNetworkDevices API.
    link: https://developer.cisco.com/docs/dna-center/#!exports-the-credentials-of-network-devices
notes:
  - SDK Method used are
    devices.Devices.exports_the_credentials_of_network_devices,
  - Paths used are
    post /dna/intent/api/v1/networkDevices/exportCredentials,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.dnac.network_devices_export_credentials_create:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    exportSshKey: true
    networkDeviceIds:
      - string
    password: string
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

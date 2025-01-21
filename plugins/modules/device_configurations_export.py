#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: device_configurations_export
short_description: Resource module for Device Configurations Export
description:
- This module represents an alias of the module device_configurations_export_v1
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  deviceId:
    description: UUIDs of the devices for which configurations need to be exported.
    elements: str
    type: list
  password:
    description: Password for the zip file to protect exported configurations. Must
      contain, at minimum 8 characters, one lowercase letter, one uppercase letter,
      one number, one special character(-=;,./~!@#$%^&*()_+{}| ?). It may not contain
      white space or the characters <>.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Configuration Archive ExportDeviceConfigurationsV1
  description: Complete reference of the ExportDeviceConfigurationsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!export-device-configurations
notes:
  - SDK Method used are
    configuration_archive.ConfigurationArchive.export_device_configurations_v1,

  - Paths used are
    post /dna/intent/api/v1/network-device-archive/cleartext,
  - It should be noted that this module is an alias of device_configurations_export_v1

"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.device_configurations_export:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    deviceId:
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

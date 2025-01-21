#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: network_device_user_defined_field_delete
short_description: Resource module for Network Device User Defined Field Delete
description:
- This module represents an alias of the module network_device_user_defined_field_delete_v1
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  deviceId:
    description: DeviceId path parameter. UUID of device from which UDF has to be removed.
    type: str
  name:
    description: Name query parameter. Name of UDF to be removed.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Devices RemoveUserDefinedFieldFromDeviceV1
  description: Complete reference of the RemoveUserDefinedFieldFromDeviceV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!remove-user-defined-field-from-device
notes:
  - SDK Method used are
    devices.Devices.remove_user_defined_field_from_device_v1,

  - Paths used are
    delete /dna/intent/api/v1/network-device/{deviceId}/user-defined-field,
  - It should be noted that this module is an alias of network_device_user_defined_field_delete_v1

"""

EXAMPLES = r"""
- name: Delete all
  cisco.dnac.network_device_user_defined_field_delete:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    deviceId: string
    name: string

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

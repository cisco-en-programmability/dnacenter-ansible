#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: device_reboot_apreboot_v1
short_description: Resource module for Device Reboot Apreboot V1
description:
- Manage operation create of the resource Device Reboot Apreboot V1.
- Users can reboot multiple access points up-to 200 at a time using this API.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  apMacAddresses:
    description: The ethernet MAC address of the access point.
    elements: str
    type: list
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Wireless RebootAccessPointsV1
  description: Complete reference of the RebootAccessPointsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!reboot-access-points
notes:
  - SDK Method used are
    wireless.Wireless.reboot_access_points_v1,

  - Paths used are
    post /dna/intent/api/v1/device-reboot/apreboot,

"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.device_reboot_apreboot_v1:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    apMacAddresses:
    - string

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

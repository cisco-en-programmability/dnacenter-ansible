#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_provision_access_point
short_description: Resource module for Wireless Provision Access Point
description:
- Manage operation create of the resource Wireless Provision Access Point.
- Access Point Provision and ReProvision.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  payload:
    description: Wireless Provision Access Point's payload.
    suboptions:
      customApGroupName:
        description: Custom AP group name.
        type: str
      customFlexGroupName:
        description: '"Custom flex group name".'
        elements: str
        type: list
      deviceName:
        description: Device name.
        type: str
      rfProfile:
        description: Radio frequency profile name.
        type: str
      siteId:
        description: Site name hierarchy(ex Global/...).
        type: str
      siteNameHierarchy:
        description: Site name hierarchy(ex Global/...).
        type: str
      type:
        description: ApWirelessConfiguration.
        type: str
    type: list
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference to SDK documentation of current version
- name: SDK function ap_provision used
  link: >
    https://dnacentersdk.rtfd.io/en/latest/api/api.html#dnacentersdk.api.v2_2_3_3.
    wireless.Wireless.ap_provision

notes:
  - Paths used: post /dna/intent/api/v1/wireless/ap-provision
"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.wireless_provision_access_point:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    payload:

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: list
  sample: >
    [
      {
        "executionId": "string",
        "executionUrl": "string",
        "message": "string"
      }
    ]
"""

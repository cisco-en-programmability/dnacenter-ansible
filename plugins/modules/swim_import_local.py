#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: swim_import_local
short_description: Resource module for Swim Import Local
description:
- Manage operation create of the resource Swim Import Local.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  filePath:
    description: File absolute path.
    type: str
  isThirdParty:
    description: IsThirdParty query parameter. Third party Image check.
    type: bool
  thirdPartyApplicationType:
    description: ThirdPartyApplicationType query parameter. Third Party Application
      Type.
    type: str
  thirdPartyImageFamily:
    description: ThirdPartyImageFamily query parameter. Third Party image family.
    type: str
  thirdPartyVendor:
    description: ThirdPartyVendor query parameter. Third Party Vendor.
    type: str
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Swim Import Local reference
  description: Complete reference of the Swim Import Local object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.swim_import_local:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    filePath: /tmp/uploads/Test-242.bin
    isThirdParty: true
    thirdPartyApplicationType: string
    thirdPartyImageFamily: string
    thirdPartyVendor: string

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

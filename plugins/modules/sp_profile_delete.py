#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: sp_profile_delete
short_description: Resource module for Sp Profile Delete
description:
  - This module represents an alias of the module sp_profile_delete_v2
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  spProfileName:
    description: SpProfileName path parameter. SP profile name.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Network Settings DeleteSPProfileV2
    description: Complete reference of the DeleteSPProfileV2 API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-sp-profile
notes:
  - SDK Method used are network_settings.NetworkSettings.delete_sp_profile_v2,
  - Paths used are delete /dna/intent/api/v2/sp-profile/{spProfileName},
  - It should be noted that this module is an alias of sp_profile_delete_v2
"""
EXAMPLES = r"""
- name: Delete by name
  cisco.dnac.sp_profile_delete:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    spProfileName: string
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

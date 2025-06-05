#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: sites_aaa_settings
short_description: Resource module for Sites Aaa Settings
description:
  - This module represents an alias of the module sites_aaa_settings_v1
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  aaaClient:
    description: Sites Aaa Settings's aaaClient.
    suboptions:
      pan:
        description: Administration Node. Required for ISE.
        type: str
      primaryServerIp:
        description: The server to use as a primary.
        type: str
      protocol:
        description: Protocol.
        type: str
      secondaryServerIp:
        description: The server to use as a secondary.
        type: str
      serverType:
        description: Server Type.
        type: str
      sharedSecret:
        description: Shared Secret.
        type: str
    type: dict
  aaaNetwork:
    description: Sites Aaa Settings's aaaNetwork.
    suboptions:
      pan:
        description: Administration Node. Required for ISE.
        type: str
      primaryServerIp:
        description: The server to use as a primary.
        type: str
      protocol:
        description: Protocol.
        type: str
      secondaryServerIp:
        description: The server to use as a secondary.
        type: str
      serverType:
        description: Server Type.
        type: str
      sharedSecret:
        description: Shared Secret.
        type: str
    type: dict
  id:
    description: Id path parameter. Site Id.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Network Settings SetAAASettingsForASiteV1
    description: Complete reference of the SetAAASettingsForASiteV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!set-aaa-settings-for-a-site
notes:
  - SDK Method used are network_settings.NetworkSettings.set_aaa_settings_for_a_site_v1,
  - Paths used are put /dna/intent/api/v1/sites/{id}/aaaSettings,
  - It should be noted that this module is an alias of sites_aaa_settings_v1
"""
EXAMPLES = r"""
- name: Update all
  cisco.dnac.sites_aaa_settings:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    aaaClient:
      pan: string
      primaryServerIp: string
      protocol: string
      secondaryServerIp: string
      serverType: string
      sharedSecret: string
    aaaNetwork:
      pan: string
      primaryServerIp: string
      protocol: string
      secondaryServerIp: string
      serverType: string
      sharedSecret: string
    id: string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "version": "string",
      "response": {
        "url": "string",
        "taskId": "string"
      }
    }
"""

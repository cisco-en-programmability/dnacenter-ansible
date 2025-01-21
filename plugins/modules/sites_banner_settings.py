#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: sites_banner_settings
short_description: Resource module for Sites Banner Settings
description:
- This module represents an alias of the module sites_banner_settings_v1
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  banner:
    description: Sites Banner Settings's banner.
    suboptions:
      message:
        description: Custom message that appears when logging into routers, switches,
          and hubs. Required for custom type.
        type: str
      type:
        description: Type.
        type: str
    type: dict
  id:
    description: Id path parameter. Site Id.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Network Settings SetBannerSettingsForASiteV1
  description: Complete reference of the SetBannerSettingsForASiteV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!set-banner-settings-for-a-site
notes:
  - SDK Method used are
    network_settings.NetworkSettings.set_banner_settings_for_a_site_v1,

  - Paths used are
    put /dna/intent/api/v1/sites/{id}/bannerSettings,
  - It should be noted that this module is an alias of sites_banner_settings_v1

"""

EXAMPLES = r"""
- name: Update all
  cisco.dnac.sites_banner_settings:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    banner:
      message: string
      type: string
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

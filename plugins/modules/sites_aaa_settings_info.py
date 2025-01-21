#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: sites_aaa_settings_info
short_description: Information module for Sites Aaa Settings Info
description:
- This module represents an alias of the module sites_aaa_settings_v1_info
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
    - Id path parameter. Site Id.
    type: str
  _inherited:
    description:
    - >
      _inherited query parameter. Include settings explicitly set for this site and settings inherited from sites
      higher in the site hierarchy; when `false`, `null` values indicate that the site inherits that setting from
      the parent site or a site higher in the site hierarchy.
    type: bool
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Network Settings RetrieveAAASettingsForASiteV1
  description: Complete reference of the RetrieveAAASettingsForASiteV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!retrieve-aaa-settings-for-a-site
notes:
  - SDK Method used are
    network_settings.NetworkSettings.retrieve_aaa_settings_for_a_site_v1,

  - Paths used are
    get /dna/intent/api/v1/sites/{id}/aaaSettings,
  - It should be noted that this module is an alias of sites_aaa_settings_v1_info

"""

EXAMPLES = r"""
- name: Get all Sites Aaa Settings Info
  cisco.dnac.sites_aaa_settings_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    _inherited: True
    id: string
  register: result

"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "aaaNetwork": {
          "serverType": "string",
          "protocol": "string",
          "pan": "string",
          "primaryServerIp": "string",
          "secondaryServerIp": "string",
          "sharedSecret": "string",
          "inheritedSiteId": "string",
          "inheritedSiteName": "string"
        },
        "aaaClient": {
          "serverType": "string",
          "protocol": "string",
          "pan": "string",
          "primaryServerIp": "string",
          "secondaryServerIp": "string",
          "sharedSecret": "string",
          "inheritedSiteId": "string",
          "inheritedSiteName": "string"
        }
      },
      "version": "string"
    }
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: sites_dhcp_settings
short_description: Resource module for Sites Dhcp Settings
description:
- This module represents an alias of the module sites_dhcp_settings_v1
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  dhcp:
    description: Sites Dhcp Settings's dhcp.
    suboptions:
      servers:
        description: DHCP servers for managing client device networking configuration.
          Max 10.
        elements: str
        type: list
    type: dict
  id:
    description: Id path parameter. Site Id.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Network Settings SetDhcpSettingsForASiteV1
  description: Complete reference of the SetDhcpSettingsForASiteV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!set-dhcp-settings-for-a-site
notes:
  - SDK Method used are
    network_settings.NetworkSettings.set_dhcp_settings_for_a_site_v1,

  - Paths used are
    put /dna/intent/api/v1/sites/{id}/dhcpSettings,
  - It should be noted that this module is an alias of sites_dhcp_settings_v1

"""

EXAMPLES = r"""
- name: Update all
  cisco.dnac.sites_dhcp_settings:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    dhcp:
      servers:
      - string
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

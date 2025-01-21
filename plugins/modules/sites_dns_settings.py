#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: sites_dns_settings
short_description: Resource module for Sites Dns Settings
description:
- This module represents an alias of the module sites_dns_settings_v1
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  dns:
    description: Sites Dns Settings's dns.
    suboptions:
      dnsServers:
        description: DNS servers for hostname resolution.
        elements: str
        type: list
      domainName:
        description: Network's domain name. Example myCompnay.com.
        type: str
    type: dict
  id:
    description: Id path parameter. Site Id.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Network Settings SetDNSSettingsForASiteV1
  description: Complete reference of the SetDNSSettingsForASiteV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!set-dns-settings-for-a-site
notes:
  - SDK Method used are
    network_settings.NetworkSettings.set_d_n_s_settings_for_a_site_v1,

  - Paths used are
    put /dna/intent/api/v1/sites/{id}/dnsSettings,
  - It should be noted that this module is an alias of sites_dns_settings_v1

"""

EXAMPLES = r"""
- name: Update all
  cisco.dnac.sites_dns_settings:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    dns:
      dnsServers:
      - string
      domainName: string
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

#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: wireless_accesspoint_configuration_summary_info
short_description: Information module for Wireless Accesspoint Configuration Summary Info
description:
- This module represents an alias of the module wireless_accesspoint_configuration_summary_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  key:
    description:
    - Key query parameter. The ethernet MAC address of Access point.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Wireless GetAccessPointConfigurationV1
  description: Complete reference of the GetAccessPointConfigurationV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-access-point-configuration-v-1
notes:
  - SDK Method used are
    wireless.Wireless.get_access_point_configuration_v1,

  - Paths used are
    get /dna/intent/api/v1/wireless/accesspoint-configuration/summary,
  - It should be noted that this module is an alias of wireless_accesspoint_configuration_summary_v1_info

"""

EXAMPLES = r"""
- name: Get all Wireless Accesspoint Configuration Summary Info
  cisco.dnac.wireless_accesspoint_configuration_summary_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    key: string
  register: result

"""
RETURN = r"""
dnac_response:
  This alias returns the output of wireless_accesspoint_configuration_summary_v1_info.
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: business_sda_wireless_controller_create
short_description: Resource module for Business Sda Wireless Controller Create
description:
- This module represents an alias of the module business_sda_wireless_controller_create_v1
version_added: '4.0.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  deviceName:
    description: WLC Device Name.
    type: str
  siteNameHierarchy:
    description: Fabric Site Name Hierarchy.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Fabric Wireless AddWLCToFabricDomainV1
  description: Complete reference of the AddWLCToFabricDomainV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!add-wlc-to-fabric-domain
notes:
  - SDK Method used are
    fabric_wireless.FabricWireless.add_w_l_c_to_fabric_domain_v1,

  - Paths used are
    post /dna/intent/api/v1/business/sda/wireless-controller,
  - It should be noted that this module is an alias of business_sda_wireless_controller_create_v1

  - Removed 'deviceIPAddress' options in v4.3.0.
"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.business_sda_wireless_controller_create:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    deviceName: string
    siteNameHierarchy: string

"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "executionId": "string",
      "executionStatusUrl": "string",
      "message": "string"
    }
"""

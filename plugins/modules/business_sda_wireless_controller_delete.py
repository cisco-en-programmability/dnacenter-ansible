#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: business_sda_wireless_controller_delete
short_description: Resource module for Business Sda Wireless Controller Delete
description:
- Manage operation delete of the resource Business Sda Wireless Controller Delete.
- Remove WLC from Fabric Domain.
version_added: '4.0.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  deviceIPAddress:
    description: DeviceIPAddress query parameter. Device Management IP Address.
    type: str
  deviceName:
    description: EWLC Device Name.
    type: str
  siteNameHierarchy:
    description: Site Name Hierarchy.
    type: str
requirements:
- dnacentersdk >= 2.4.4
- python >= 3.5
notes:
  - SDK Method used are
    fabric_wireless.FabricWireless.add_w_l_c_to_fabric_domain
  - Paths used are delete /dna/intent/api/v1/business/sda/wireless-controller
"""

EXAMPLES = r"""
- name: Delete all
  cisco.dnac.business_sda_wireless_controller_delete:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    deviceIPAddress: string

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

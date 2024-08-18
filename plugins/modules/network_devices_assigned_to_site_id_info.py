#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: networkDevices_assignedToSite_id_info
short_description: Information module for Networkdevices Assignedtosite Id
description:
- Get all Networkdevices Assignedtosite Id.
- >
   Get site assigned network device. The items in the list are arranged in an order that corresponds with their
   internal identifiers.
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
    - Id path parameter. Network Device Id.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Site Design GetSiteAssignedNetworkDevice
  description: Complete reference of the GetSiteAssignedNetworkDevice API.
  link: https://developer.cisco.com/docs/dna-center/#!get-site-assigned-network-device
notes:
  - SDK Method used are
    site_design.SiteDesign.get_site_assigned_network_device,

  - Paths used are
    get /dna/intent/api/v1/networkDevices/{id}/assignedToSite,

"""

EXAMPLES = r"""
- name: Get all Networkdevices Assignedtosite Id
  cisco.dnac.networkDevices_assignedToSite_id_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
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
        "deviceId": "string",
        "siteId": "string",
        "siteNameHierarchy": "string",
        "siteType": "string"
      },
      "version": "string"
    }
"""

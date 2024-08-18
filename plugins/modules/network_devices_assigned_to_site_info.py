#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: networkDevices_assignedToSite_info
short_description: Information module for Networkdevices Assignedtosite
description:
- Get all Networkdevices Assignedtosite.
- >
   Get all site assigned network devices. The items in the list are arranged in an order that corresponds with their
   internal identifiers.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  siteId:
    description:
    - SiteId query parameter. Site Id. It must be area Id or building Id or floor Id.
    type: str
  offset:
    description:
    - Offset query parameter. The first record to show for this page; the first record is numbered 1.
    type: float
  limit:
    description:
    - Limit query parameter. The number of records to show for this page.
    type: float
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Site Design GetSiteAssignedNetworkDevices
  description: Complete reference of the GetSiteAssignedNetworkDevices API.
  link: https://developer.cisco.com/docs/dna-center/#!get-site-assigned-network-devices
notes:
  - SDK Method used are
    site_design.SiteDesign.get_site_assigned_network_devices,

  - Paths used are
    get /dna/intent/api/v1/networkDevices/assignedToSite,

"""

EXAMPLES = r"""
- name: Get all Networkdevices Assignedtosite
  cisco.dnac.networkDevices_assignedToSite_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    siteId: string
    offset: 0
    limit: 0
  register: result

"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "deviceId": "string",
          "siteId": "string",
          "siteNameHierarchy": "string",
          "siteType": "string"
        }
      ],
      "version": "string"
    }
"""

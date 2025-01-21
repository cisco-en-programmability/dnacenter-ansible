#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: network_devices_assigned_to_site_info
short_description: Information module for Network Devices Assigned To Site Info
description:
- This module represents an alias of the module network_devices_assigned_to_site_v1_info
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
    - Limit query parameter. The number of records to show for this page;The minimum is 1, and the maximum is 500.
    type: float
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Site Design GetSiteAssignedNetworkDevicesV1
  description: Complete reference of the GetSiteAssignedNetworkDevicesV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-site-assigned-network-devices
notes:
  - SDK Method used are
    site_design.SiteDesign.get_site_assigned_network_devices_v1,

  - Paths used are
    get /dna/intent/api/v1/networkDevices/assignedToSite,
  - It should be noted that this module is an alias of network_devices_assigned_to_site_v1_info

"""

EXAMPLES = r"""
- name: Get all Network Devices Assigned To Site Info
  cisco.dnac.network_devices_assigned_to_site_info:
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

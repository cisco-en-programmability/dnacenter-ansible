#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: assign_to_site_apply
short_description: Resource module for Assign To Site Apply
description:
  - This module represents an alias of the module assign_to_site_apply_v1
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  deviceIds:
    description: Unassigned network devices, ranging from a minimum of 1 to a maximum
      of 100.
    elements: str
    type: list
  siteId:
    description: This must be building Id or floor Id. Access points, Sensors are
      assigned to floor. Remaining network devices are assigned to building. Site
      Id can be retrieved using '/intent/api/v1/sites'.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Site Design AssignNetworkDevicesToASiteV1
    description: Complete reference of the AssignNetworkDevicesToASiteV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!assign-network-devices-to-a-site
notes:
  - SDK Method used are site_design.SiteDesign.assign_network_devices_to_a_site_v1,
  - Paths used are post /dna/intent/api/v1/networkDevices/assignToSite/apply,
  - It should be noted that this module is an alias of assign_to_site_apply_v1
"""
EXAMPLES = r"""
- name: Create
  cisco.dnac.assign_to_site_apply:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    deviceIds:
      - string
    siteId: string
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

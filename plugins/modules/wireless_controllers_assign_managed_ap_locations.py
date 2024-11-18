#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: wireless_controllers_assign_managed_ap_locations
short_description: Resource module for Wireless Controllers Assign Managed Ap Locations
description:
- This module represents an alias of the module wireless_controllers_assign_managed_ap_locations_v1
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  deviceId:
    description: DeviceId path parameter. Network Device ID. This value can be obtained
      by using the API call GET /dna/intent/api/v1/network-device/ip-address/${ipAddress}.
    type: str
  primaryManagedAPLocationsSiteIds:
    description: Site IDs of Primary Managed AP Locations. These values can be obtained
      by using the API call GET /dna/intent/api/v1/site.
    elements: str
    type: list
  secondaryManagedAPLocationsSiteIds:
    description: Site IDs of Secondary Managed AP Locations. These values can be obtained
      by using the API call GET /dna/intent/api/v1/site.
    elements: str
    type: list
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Wireless AssignManagedAPLocationsForWLCV1
  description: Complete reference of the AssignManagedAPLocationsForWLCV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!assign-managed-ap-locations-for-wlc-v-1
notes:
  - SDK Method used are
    wireless.Wireless.assign_managed_ap_locations_for_w_l_c_v1,

  - Paths used are
    post /dna/intent/api/v1/wirelessControllers/{deviceId}/assignManagedApLocations,
  - It should be noted that this module is an alias of wireless_controllers_assign_managed_ap_locations_v1

"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.wireless_controllers_assign_managed_ap_locations:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    deviceId: string
    primaryManagedAPLocationsSiteIds:
    - string
    secondaryManagedAPLocationsSiteIds:
    - string

"""
RETURN = r"""
dnac_response:
  description:
    - This alias returns the output of wireless_controllers_assign_managed_ap_locations_v1.
"""
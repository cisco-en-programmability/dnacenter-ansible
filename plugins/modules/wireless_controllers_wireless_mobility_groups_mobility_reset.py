#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wirelessControllers_wirelessMobilityGroups_mobilityReset
short_description: Resource module for Wirelesscontrollers Wirelessmobilitygroups Mobilityreset
description:
- Manage operation create of the resource Wirelesscontrollers Wirelessmobilitygroups Mobilityreset.
- This API is used to reset wireless mobility which in turn sets mobility group name as 'default'.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  networkDeviceId:
    description: Network device Id of Cisco wireless controller.Obtain the network device
      ID value by using the API call GET - /dna/intent/api/v1/network-device/ip-address/${ipAddress}.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Wireless MobilityReset
  description: Complete reference of the MobilityReset API.
  link: https://developer.cisco.com/docs/dna-center/#!mobility-reset
notes:
  - SDK Method used are
    wireless.Wireless.mobility_reset,

  - Paths used are
    post /dna/intent/api/v1/wirelessControllers/wirelessMobilityGroups/mobilityReset,

"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.wirelessControllers_wirelessMobilityGroups_mobilityReset:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    networkDeviceId: string

"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""

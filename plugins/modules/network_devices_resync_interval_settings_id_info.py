#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: networkDevices_resyncIntervalSettings_id_info
short_description: Information module for Networkdevices Resyncintervalsettings Id
description:
- Get all Networkdevices Resyncintervalsettings Id.
- Fetch the reysnc interval for the given network device id.
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
    - Id path parameter. The id of the network device.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Devices GetResyncIntervalForTheNetworkDevice
  description: Complete reference of the GetResyncIntervalForTheNetworkDevice API.
  link: https://developer.cisco.com/docs/dna-center/#!get-resync-interval-for-the-network-device
notes:
  - SDK Method used are
    devices.Devices.get_resync_interval_for_the_network_device,

  - Paths used are
    get /dna/intent/api/v1/networkDevices/{id}/resyncIntervalSettings,

"""

EXAMPLES = r"""
- name: Get all Networkdevices Resyncintervalsettings Id
  cisco.dnac.networkDevices_resyncIntervalSettings_id_info:
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
        "interval": 0
      },
      "version": "string"
    }
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: network_bugs_results_bugs_id_network_devices_count_info
short_description: Information module for Network Bugs Results Bugs Id Network Devices
  Count Info
description:
  - This module represents an alias of the module network_bugs_results_bugs_id_network_devices_count_v1_info
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id path parameter. Id of the network bug.
    type: str
  networkDeviceId:
    description:
      - NetworkDeviceId query parameter. Id of the network device.
    type: str
  scanMode:
    description:
      - >
        ScanMode query parameter. Mode or the criteria using which the network device
        was scanned. Available values
        ESSENTIALS, ADVANTAGE, CX_CLOUD, NOT_AVAILABLE.
    type: str
  scanStatus:
    description:
      - >
        ScanStatus query parameter. Status of the scan on the network device. Available
        values NOT_SCANNED,
        IN_PROGRESS, SUCCESS, FAILED, FALL_BACK.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Compliance GetCountOfNetworkBugDevicesForTheBugV1
    description: Complete reference of the GetCountOfNetworkBugDevicesForTheBugV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!get-count-of-network-bug-devices-for-the-bug
notes:
  - SDK Method used are compliance.Compliance.get_count_of_network_bug_devices_for_the_bug_v1,
  - Paths used are get /dna/intent/api/v1/networkBugs/results/bugs/{id}/networkDevices/count,
  - It should be noted that this module is an alias of network_bugs_results_bugs_id_network_devices_count_v1_info
"""
EXAMPLES = r"""
- name: Get all Network Bugs Results Bugs Id Network Devices Count Info
  cisco.dnac.network_bugs_results_bugs_id_network_devices_count_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    networkDeviceId: string
    scanMode: string
    scanStatus: string
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
      "version": "string",
      "response": {
        "count": 0
      }
    }
"""

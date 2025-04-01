#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: network_bugs_results_network_devices_network_device_id_bugs_count_info
short_description: Information module for Network Bugs Results Network Devices Network
  Device Id Bugs Count Info
description:
  - This module represents an alias of the module network_bugs_results_network_devices_network_device_id_bugs_count_v1_info
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  networkDeviceId:
    description:
      - NetworkDeviceId path parameter. Id of the network device.
    type: str
  id:
    description:
      - Id query parameter. Id of the network bug.
    type: str
  severity:
    description:
      - Severity query parameter. Return network bugs with this severity. Available
        values CATASTROPHIC, SEVERE, MODERATE.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Compliance GetCountOfBugsAffectingTheNetworkDeviceV1
    description: Complete reference of the GetCountOfBugsAffectingTheNetworkDeviceV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!get-count-of-bugs-affecting-the-network-device
notes:
  - SDK Method used are compliance.Compliance.get_count_of_bugs_affecting_the_network_device_v1,
  - Paths used are get
    /dna/intent/api/v1/networkBugs/results/networkDevices/{networkDeviceId}/bugs/count,
  - It should be noted that this module is an alias of network_bugs_results_network_devices_network_device_id_bugs_count_v1_info
"""
EXAMPLES = r"""
- name: Get all Network Bugs Results Network Devices Network Device Id Bugs Count
    Info
  cisco.dnac.network_bugs_results_network_devices_network_device_id_bugs_count_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
    severity: string
    networkDeviceId: string
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

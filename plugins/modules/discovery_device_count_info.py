#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: discovery_device_count_info
short_description: Information module for Discovery Device Count Info
description:
  - This module represents an alias of the module discovery_device_count_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id path parameter. Discovery ID.
    type: str
  taskId:
    description:
      - TaskId query parameter.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Discovery GetDevicesDiscoveredByIdV1
    description: Complete reference of the GetDevicesDiscoveredByIdV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-devices-discovered-by-id
notes:
  - SDK Method used are discovery.Discovery.get_devices_discovered_by_id_v1,
  - Paths used are get /dna/intent/api/v1/discovery/{id}/network-device/count,
  - It should be noted that this module is an alias of discovery_device_count_v1_info
"""
EXAMPLES = r"""
- name: Get all Discovery Device Count Info
  cisco.dnac.discovery_device_count_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    taskId: string
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
      "response": 0,
      "version": "string"
    }
"""

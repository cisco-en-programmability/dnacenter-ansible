#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: field_notices_results_notices_id_network_devices_count_info
short_description: Information module for Field Notices Results Notices Id Network Devices Count Info
description:
- This module represents an alias of the module field_notices_results_notices_id_network_devices_count_v1_info
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
    - Id path parameter. Id of the field notice.
    type: str
  networkDeviceId:
    description:
    - NetworkDeviceId query parameter. Id of the network device.
    type: str
  scanStatus:
    description:
    - >
      ScanStatus query parameter. Status of the scan on the network device. Available values NOT_SCANNED,
      IN_PROGRESS, SUCCESS, FAILED.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Compliance GetCountOfFieldNoticeNetworkDevicesForTheNoticeV1
  description: Complete reference of the GetCountOfFieldNoticeNetworkDevicesForTheNoticeV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-count-of-field-notice-network-devices-for-the-notice
notes:
  - SDK Method used are
    compliance.Compliance.get_count_of_field_notice_network_devices_for_the_notice_v1,

  - Paths used are
    get /dna/intent/api/v1/fieldNotices/results/notices/{id}/networkDevices/count,
  - It should be noted that this module is an alias of field_notices_results_notices_id_network_devices_count_v1_info

"""

EXAMPLES = r"""
- name: Get all Field Notices Results Notices Id Network Devices Count Info
  cisco.dnac.field_notices_results_notices_id_network_devices_count_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    networkDeviceId: string
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

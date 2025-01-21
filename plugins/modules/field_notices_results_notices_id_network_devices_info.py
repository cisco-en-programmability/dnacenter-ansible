#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: field_notices_results_notices_id_network_devices_info
short_description: Information module for Field Notices Results Notices Id Network Devices Info
description:
- This module represents an alias of the module field_notices_results_notices_id_network_devices_v1_info
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
  offset:
    description:
    - Offset query parameter. The first record to show for this page; the first record is numbered 1. Default value is 1.
    type: float
  limit:
    description:
    - >
      Limit query parameter. The number of records to show for this page. Minimum value is 1. Maximum value is
      500. Default value is 500.
    type: float
  sortBy:
    description:
    - SortBy query parameter. A property within the response to sort by.
    type: str
  order:
    description:
    - >
      Order query parameter. Whether ascending or descending order should be used to sort the response. Available
      values asc, desc. Default value is asc.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Compliance GetFieldNoticeNetworkDevicesForTheNoticeV1
  description: Complete reference of the GetFieldNoticeNetworkDevicesForTheNoticeV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-field-notice-network-devices-for-the-notice
notes:
  - SDK Method used are
    compliance.Compliance.get_field_notice_network_devices_for_the_notice_v1,

  - Paths used are
    get /dna/intent/api/v1/fieldNotices/results/notices/{id}/networkDevices,
  - It should be noted that this module is an alias of field_notices_results_notices_id_network_devices_v1_info

"""

EXAMPLES = r"""
- name: Get all Field Notices Results Notices Id Network Devices Info
  cisco.dnac.field_notices_results_notices_id_network_devices_info:
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
    offset: 0
    limit: 0
    sortBy: string
    order: string
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
      "response": [
        {
          "networkDeviceId": "string",
          "noticeCount": 0,
          "potentialNoticeCount": 0,
          "scanStatus": "string",
          "comments": "string",
          "lastScanTime": 0
        }
      ],
      "version": "string"
    }
"""

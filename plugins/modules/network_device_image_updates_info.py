#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: network_device_image_updates_info
short_description: Information module for Network Device Image Updates Info
description:
- This module represents an alias of the module network_device_image_updates_v1_info
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
    - Id query parameter. Update id which is unique for each network device under the parentId.
    type: str
  parentId:
    description:
    - ParentId query parameter. Updates that have this parent id.
    type: str
  networkDeviceId:
    description:
    - NetworkDeviceId query parameter. Network device id.
    type: str
  status:
    description:
    - Status query parameter. Status of the image update. Available values FAILURE, SUCCESS, IN_PROGRESS, PENDING.
    type: str
  imageName:
    description:
    - ImageName query parameter. Software image name for the update.
    type: str
  hostName:
    description:
    - >
      HostName query parameter. Host name of the network device for the image update. Supports case-insensitive
      partial search.
    type: str
  managementAddress:
    description:
    - ManagementAddress query parameter. Management address of the network device.
    type: str
  startTime:
    description:
    - StartTime query parameter. Image update started after the given time (as milliseconds since UNIX epoch).
    type: float
  endTime:
    description:
    - EndTime query parameter. Image update started before the given time (as milliseconds since UNIX epoch).
    type: float
  sortBy:
    description:
    - SortBy query parameter. A property within the response to sort by.
    type: str
  order:
    description:
    - Order query parameter. Whether ascending or descending order should be used to sort the response.
    type: str
  offset:
    description:
    - Offset query parameter. The first record to show for this page; the first record is numbered 1.
    type: float
  limit:
    description:
    - >
      Limit query parameter. The number of records to show for this page. The minimum and maximum values are 1 and
      500, respectively.
    type: float
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Software Image Management (SWIM) GetNetworkDeviceImageUpdatesV1
  description: Complete reference of the GetNetworkDeviceImageUpdatesV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-network-device-image-updates
notes:
  - SDK Method used are
    software_image_management_swim.SoftwareImageManagementSwim.get_network_device_image_updates_v1,

  - Paths used are
    get /dna/intent/api/v1/networkDeviceImageUpdates,
  - It should be noted that this module is an alias of network_device_image_updates_v1_info

"""

EXAMPLES = r"""
- name: Get all Network Device Image Updates Info
  cisco.dnac.network_device_image_updates_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
    parentId: string
    networkDeviceId: string
    status: string
    imageName: string
    hostName: string
    managementAddress: string
    startTime: 0
    endTime: 0
    sortBy: string
    order: string
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
          "id": "string",
          "parentId": "string",
          "startTime": 0,
          "endTime": 0,
          "status": "string",
          "networkDeviceId": "string",
          "managementAddress": "string",
          "hostName": "string",
          "updateImageVersion": "string",
          "type": "string"
        }
      ],
      "version": "string"
    }
"""

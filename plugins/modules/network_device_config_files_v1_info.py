#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_device_config_files_v1_info
short_description: Information module for Network Device Config Files V1
description:
- Get all Network Device Config Files V1.
- >
   Retrieves the list of network device configuration file details, sorted by createdTime in descending order. Use
   /intent/api/v1/networkDeviceConfigFiles/{id}/downloadMasked to download masked configurations, or
   /intent/api/v1/networkDeviceConfigFiles/{id}/downloadUnmasked for unmasked configurations.
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
    - Id query parameter. Unique identifier (UUID) of the configuration file.
    type: str
  networkDeviceId:
    description:
    - >
      NetworkDeviceId query parameter. Unique identifier (UUID) of the network devices. The number of
      networkDeviceId(s) must not exceed 5.
    type: str
  fileType:
    description:
    - >
      FileType query parameter. Type of device configuration file.Available values 'RUNNINGCONFIG',
      'STARTUPCONFIG', 'VLAN'.
    type: str
  offset:
    description:
    - Offset query parameter. The first record to show for this page; the first record is numbered 1.
    type: float
  limit:
    description:
    - >
      Limit query parameter. The number of records to be retrieved defaults to 500 if not specified, with a
      maximum allowed limit of 500.
    type: float
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Configuration Archive GetNetworkDeviceConfigurationFileDetailsV1
  description: Complete reference of the GetNetworkDeviceConfigurationFileDetailsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-network-device-configuration-file-details
notes:
  - SDK Method used are
    configuration_archive.ConfigurationArchive.get_network_device_configuration_file_details_v1,

  - Paths used are
    get /dna/intent/api/v1/networkDeviceConfigFiles,

"""

EXAMPLES = r"""
- name: Get all Network Device Config Files V1
  cisco.dnac.network_device_config_files_v1_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
    networkDeviceId: string
    fileType: string
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
          "networkDeviceId": "string",
          "versionId": "string",
          "fileType": "string",
          "createdBy": "string",
          "createdTime": 0
        }
      ],
      "version": "string"
    }
"""

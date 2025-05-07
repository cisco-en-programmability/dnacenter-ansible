#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: network_device_config_files_id_v1_info
short_description: Information module for Network Device Config Files Id V1
description:
  - Get Network Device Config Files Id V1 by id.
  - Retrieves the details of a specific network device configuration file using the
    `id`.
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
      - >
        Id path parameter. The value of `id` can be obtained from the response of
        API
        `/dna/intent/api/v1/networkDeviceConfigFiles`.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Configuration Archive GetConfigurationFileDetailsByIDV1
    description: Complete reference of the GetConfigurationFileDetailsByIDV1 API.
    link:
      https://developer.cisco.com/docs/dna-center/#!get-configuration-file-details-by-id
notes:
  - SDK Method used are
    configuration_archive.ConfigurationArchive.get_configuration_file_details_by_id_v1,
  - Paths used are get /dna/intent/api/v1/networkDeviceConfigFiles/{id},
"""
EXAMPLES = r"""
- name: Get Network Device Config Files Id V1 by id
  cisco.dnac.network_device_config_files_id_v1_info:
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
        "id": "string",
        "networkDeviceId": "string",
        "versionId": "string",
        "fileType": "string",
        "createdBy": "string",
        "createdTime": "string"
      },
      "version": "string"
    }
"""

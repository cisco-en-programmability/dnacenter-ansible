#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: images_distribution_server_settings_info
short_description: Information module for Images Distribution Server Settings Info
description:
  - This module represents an alias of the module images_distribution_server_settings_v1_info
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Software Image Management (SWIM) RetrieveImageDistributionServersV1
    description: Complete reference of the RetrieveImageDistributionServersV1 API.
    link:
      https://developer.cisco.com/docs/dna-center/#!retrieve-image-distribution-servers
notes:
  - SDK Method used are
    software_image_management_swim.SoftwareImageManagementSwim.retrieve_image_distribution_servers_v1,
  - Paths used are get /dna/intent/api/v1/images/distributionServerSettings,
  - It should be noted that this module is an alias of images_distribution_server_settings_v1_info
"""
EXAMPLES = r"""
- name: Get all Images Distribution Server Settings Info
  cisco.dnac.images_distribution_server_settings_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
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
          "username": "string",
          "serverAddress": "string",
          "portNumber": 0,
          "rootLocation": "string"
        }
      ],
      "version": "string"
    }
"""

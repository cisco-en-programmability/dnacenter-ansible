#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: images_addon_images_count_info
short_description: Information module for Images Addon Images Count Info
description:
  - This module represents an alias of the module images_addon_images_count_v1_info
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
      - Id path parameter. Software image identifier. Check API `/dna/intent/api/v1/images`
        for id from response.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Software Image Management (SWIM) ReturnsCountOfAddOnImagesV1
    description: Complete reference of the ReturnsCountOfAddOnImagesV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!returns-count-of-add-on-images
notes:
  - SDK Method used are
    software_image_management_swim.SoftwareImageManagementSwim.returns_count_of_add_on_images_v1,
  - Paths used are get /dna/intent/api/v1/images/{id}/addonImages/count,
  - It should be noted that this module is an alias of images_addon_images_count_v1_info
"""
EXAMPLES = r"""
- name: Get all Images Addon Images Count Info
  cisco.dnac.images_addon_images_count_info:
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
        "count": 0
      },
      "version": "string"
    }
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: images_download_v1
short_description: Resource module for Images Download V1
description:
  - Manage operation create of the resource Images Download V1.
  - >
    Initiates download of the software image from Cisco.com on the disk for the given
    `id`. Refer to
    `/dna/intent/api/v1/images` for obtaining `id`.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter. Software image identifier. Check API `/dna/intent/api/v1/images`
      for `id` from response.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Software Image Management (SWIM) DownloadTheSoftwareImageV1
    description: Complete reference of the DownloadTheSoftwareImageV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!download-the-software-image
notes:
  - SDK Method used are
    software_image_management_swim.SoftwareImageManagementSwim.download_the_software_image_v1,
  - Paths used are post /dna/intent/api/v1/images/{id}/download,
"""
EXAMPLES = r"""
- name: Create
  cisco.dnac.images_download_v1:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    id: string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""

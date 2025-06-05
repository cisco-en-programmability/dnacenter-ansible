#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: images_id
short_description: Resource module for Images Id
description:
  - This module represents an alias of the module images_id_v1
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter. The software image identifier that needs to be
      deleted can be obtained from the API `/dna/intent/api/v1/images?imported=true`.
      Use this API to obtain the `id` of the image.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Software Image Management (SWIM) DeleteImageV1
    description: Complete reference of the DeleteImageV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-image
notes:
  - SDK Method used are software_image_management_swim.SoftwareImageManagementSwim.delete_image_v1,
  - Paths used are delete /dna/intent/api/v1/images/{id},
  - It should be noted that this module is an alias of images_id_v1
"""
EXAMPLES = r"""
- name: Delete by id
  cisco.dnac.images_id:
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

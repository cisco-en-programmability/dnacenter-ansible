#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: floors_upload_image
short_description: Resource module for Floors Upload Image
description:
  - This module represents an alias of the module floors_upload_image_v2
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter. Floor Id.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Site Design UploadsFloorImageV2
    description: Complete reference of the UploadsFloorImageV2 API.
    link: https://developer.cisco.com/docs/dna-center/#!uploads-floor-image
notes:
  - SDK Method used are site_design.SiteDesign.uploads_floor_image_v2,
  - Paths used are post /dna/intent/api/v2/floors/{id}/uploadImage,
  - It should be noted that this module is an alias of floors_upload_image_v2
"""
EXAMPLES = r"""
- name: Create
  cisco.dnac.floors_upload_image:
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
    {}
"""

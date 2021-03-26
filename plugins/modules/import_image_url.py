#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    "metadata_version": "0.0.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
---
module: import_image_url
short_description: Manage ImportImageUrl objects of SoftwareImageManagementSwim
description:
- Fetches a software image from remote file system (using URL for HTTP/FTP) and uploads to DNA Center. Supported image files extensions are bin, img, tar, smu, pie, aes, iso, ova, tar_gz and qcow2.
version_added: '1.0'
author: Rafael Campos (@racampos)
options:
  schedule_at:
    description:
    - Epoch Time (The number of milli-seconds since January 1 1970 UTC) at which the distribution should be scheduled (Optional) .
    type: str
  schedule_desc:
    description:
    - Custom Description (Optional).
    type: str
  schedule_origin:
    description:
    - Originator of this call (Optional).
    type: str
  payload:
    description:
    - An object to send in the Request body.
    type: list
    required: True
    elements: dict
    suboptions:
      applicationType:
        description:
        - It is the import image url's applicationType.
        type: str
      imageFamily:
        description:
        - It is the import image url's imageFamily.
        type: str
      sourceURL:
        description:
        - It is the import image url's sourceURL.
        type: str
      thirdParty:
        description:
        - It is the import image url's thirdParty.
        type: bool
      vendor:
        description:
        - It is the import image url's vendor.
        type: str


requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.import_image_url
# Reference by Internet resource
- name: ImportImageUrl reference
  description: Complete reference of the ImportImageUrl object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: ImportImageUrl reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: import_software_image_via_url
  cisco.dnac.import_image_url:
    state: create  # required
    payload:  # required
    - applicationType: SomeValue  # string
      imageFamily: SomeValue  # string
      sourceURL: SomeValue  # string
      thirdParty: True  # boolean
      vendor: SomeValue  # string
    schedule_at: SomeValue  # string
    schedule_desc: SomeValue  # string
    schedule_origin: SomeValue  # string
  """

RETURN = """
import_software_image_via_url:
    description: Fetches a software image from remote file system (using URL for HTTP/FTP) and uploads to DNA Center. Supported image files extensions are bin, img, tar, smu, pie, aes, iso, ova, tar_gz and qcow2.
    returned: success
    type: dict
    contains:
    response:
      description: ImageImportFromUrlDTO's response.
      returned: success
      type: dict
      contains:
        taskId:
          description: It is the import image url's taskId.
          returned: success
          type: dict
        url:
          description: It is the import image url's url.
          returned: success
          type: str
          sample: '<url>'

    version:
      description: ImageImportFromUrlDTO's version.
      returned: success
      type: str
      sample: '1.0'

"""

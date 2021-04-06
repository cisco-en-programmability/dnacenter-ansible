#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: import_image_url
short_description: Manage ImportImageUrl objects of SoftwareImageManagementSwim
description:
- >
   Fetches a software image from remote file system (using URL for HTTP/FTP) and uploads to DNA Center. Supported image files extensions are bin,
   img, tar, smu, pie, aes, iso, ova, tar_gz and qcow2.
version_added: '1.0.0'
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

RETURN = r"""
dnac_response:
  description: A dictionary with the response returned by the DNA Center Python SDK
  returned: always
  type: dict
  sample: {"response": 29, "version": "1.0"}
sdk_function:
  description: The DNA Center SDK function used to execute the task
  returned: always
  type: str
  sample: application_policy.get_application_sets
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: list
  sample:
"""

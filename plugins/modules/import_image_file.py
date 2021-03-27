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
module: import_image_file
short_description: Manage ImportImageFile objects of SoftwareImageManagementSwim
description:
- Fetches a software image from local file system and uploads to DNA Center. Supported software image files extensions are bin, img, tar, smu, pie, aes, iso, ova, tar_gz and qcow2.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  filename:
    description:
    - The filename (with its extension, for example, test.zip).
    type: str
    required: True
  filepath:
    description:
    - The full path of a file. The file is opened with rb flag.
    type: str
    required: True
  is_third_party:
    description:
    - Third party Image check.
    type: bool
  third_party_application_type:
    description:
    - Third Party Application Type.
    type: str
  third_party_image_family:
    description:
    - Third Party image family.
    type: str
  third_party_vendor:
    description:
    - Third Party Vendor.
    type: str

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.import_image_file
# Reference by Internet resource
- name: ImportImageFile reference
  description: Complete reference of the ImportImageFile object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: ImportImageFile reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: import_local_software_image
  cisco.dnac.import_image_file:
    state: create  # required
    filename: SomeValue  # string, required
    filepath: SomeValue  # string, required
    is_third_party: True  # boolean
    third_party_application_type: SomeValue  # string
    third_party_image_family: SomeValue  # string
    third_party_vendor: SomeValue  # string
  
"""

RETURN = """
"""

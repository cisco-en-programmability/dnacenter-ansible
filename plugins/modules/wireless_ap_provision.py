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
module: wireless_ap_provision
short_description: Manage WirelessApProvision objects of Wireless
description:
- Access Point Provision and ReProvision.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  payload:
    description:
    - An object to send in the Request body.
    type: list
    required: True
    elements: dict
    suboptions:
      executionId:
        description:
        - It is the wireless ap provision's executionId.
        type: str
      executionUrl:
        description:
        - It is the wireless ap provision's executionUrl.
        type: str
      message:
        description:
        - It is the wireless ap provision's message.
        type: str


requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.wireless_ap_provision
# Reference by Internet resource
- name: WirelessApProvision reference
  description: Complete reference of the WirelessApProvision object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: WirelessApProvision reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: ap_provision_and_re_provision
  cisco.dnac.wireless_ap_provision:
    state: create  # required
    payload:  # required
    - executionId: SomeValue  # string
      executionUrl: SomeValue  # string
      message: SomeValue  # string

"""

RETURN = """
"""

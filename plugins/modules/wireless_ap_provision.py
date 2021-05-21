#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Cisco Systems
# MIT License (see LICENSE)

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
  sample: wireless.ap_provision_and_re_provision
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: list
  sample:
"""

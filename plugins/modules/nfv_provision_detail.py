#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Cisco Systems
# MIT License (see LICENSE)

DOCUMENTATION = r"""
---
module: nfv_provision_detail
short_description: Manage NfvProvisionDetail objects of SiteDesign
description:
- Checks the provisioning detail of an ENCS device including log information.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  device_ip:
    description:
    - Device Ip, property of the request body.
    type: str
    required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.nfv_provision_detail
# Reference by Internet resource
- name: NfvProvisionDetail reference
  description: Complete reference of the NfvProvisionDetail object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: NfvProvisionDetail reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: nfv_provisioning_detail
  cisco.dnac.nfv_provision_detail:
    state: create  # required
    device_ip: SomeValue  # string, required

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
  sample: site_design.nfv_provisioning_detail
missing_params:
  description: Provided arguments do not comply with the schema of the DNA Center Python SDK function
  returned: when the function request schema is not satisfied
  type: list
  sample:
"""

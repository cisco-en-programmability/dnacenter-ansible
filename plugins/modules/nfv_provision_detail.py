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

RETURN = """
nfv_provisioning_detail:
    description: Checks the provisioning detail of an ENCS device including log information.
    returned: success
    type: dict
    contains:
      executionId:
      description: Execution Id, property of the response body.
      returned: success
      type: str
      sample: '<executionid>'
    executionStatusUrl:
      description: Execution Status Url, property of the response body.
      returned: success
      type: str
      sample: '<executionstatusurl>'
    message:
      description: Message, property of the response body.
      returned: success
      type: str
      sample: '<message>'

"""

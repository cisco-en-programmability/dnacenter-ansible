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
module: network_device_meraki_org
short_description: Manage NetworkDeviceMerakiOrg objects of Devices
description:
- Returns list of organizations for meraki dashboard.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  id:
    description:
    - Id path parameter.
    type: str
    required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.network_device_meraki_org
# Reference by Internet resource
- name: NetworkDeviceMerakiOrg reference
  description: Complete reference of the NetworkDeviceMerakiOrg object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: NetworkDeviceMerakiOrg reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_organization_list_for_meraki
  cisco.dnac.network_device_meraki_org:
    state: query  # required
    id: SomeValue  # string, required
  register: query_result
  
"""

RETURN = """
get_organization_list_for_meraki:
    description: Returns list of organizations for meraki dashboard.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body (list of strings).
      returned: always
      type: list
    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

"""

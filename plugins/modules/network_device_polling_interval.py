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
module: network_device_polling_interval
short_description: Manage NetworkDevicePollingInterval objects of Devices
description:
- Returns polling interval by device id.
- Returns polling interval of all devices.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  id:
    description:
    - Device ID.
    type: str
    required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.network_device_polling_interval
# Reference by Internet resource
- name: NetworkDevicePollingInterval reference
  description: Complete reference of the NetworkDevicePollingInterval object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: NetworkDevicePollingInterval reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_polling_interval_by_id
  cisco.dnac.network_device_polling_interval:
    state: query  # required
    id: SomeValue  # string, required
  register: query_result
  
- name: get_polling_interval_for_all_devices
  cisco.dnac.network_device_polling_interval:
    state: query  # required

  register: query_result
  
"""

RETURN = """
"""

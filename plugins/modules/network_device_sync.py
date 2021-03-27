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
module: network_device_sync
short_description: Manage NetworkDeviceSync objects of Devices
description:
- Synchronizes the devices. If forceSync param is false (default) then the sync would run in normal priority thread. If forceSync param is true then the sync would run in high priority thread if available, else the sync will fail. Result can be seen in the child task of each device.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  force_sync:
    description:
    - ForceSync query parameter.
    type: bool
  payload:
    description:
    - An object to send in the Request body.
    type: list
    required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.network_device_sync
# Reference by Internet resource
- name: NetworkDeviceSync reference
  description: Complete reference of the NetworkDeviceSync object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: NetworkDeviceSync reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: sync_devices_using_forcesync
  cisco.dnac.network_device_sync:
    state: update  # required
    payload: None, required
    force_sync: True  # boolean
  
"""

RETURN = """
"""

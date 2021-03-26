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
module: network_device_update_role
short_description: Manage NetworkDeviceUpdateRole objects of Devices
description:
- Updates the role of the device as access, core, distribution, border router.
version_added: '1.0'
author: Rafael Campos (@racampos)
options:
  id:
    description:
    - NetworkDeviceBriefNIO's id.
    type: str
    required: True
  role:
    description:
    - NetworkDeviceBriefNIO's role.
    type: str
    required: True
  roleSource:
    description:
    - NetworkDeviceBriefNIO's roleSource.
    type: str
    required: True
  summary:
    description:
    - If true gets the summary.
    type: bool
    required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.network_device_update_role
# Reference by Internet resource
- name: NetworkDeviceUpdateRole reference
  description: Complete reference of the NetworkDeviceUpdateRole object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: NetworkDeviceUpdateRole reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: update_device_role
  cisco.dnac.network_device_update_role:
    state: update  # required
    id: SomeValue  # string, required
    role: SomeValue  # string, required
    roleSource: SomeValue  # string, required
    summary: True  # boolean, required
  """

RETURN = """
update_device_role:
    description: Updates the role of the device as access, core, distribution, border router.
    returned: changed
    type: dict
    contains:
    response:
      description: NetworkDeviceBriefNIO's response.
      returned: changed
      type: dict
      contains:
        taskId:
          description: It is the network device update role's taskId.
          returned: changed
          type: dict
        url:
          description: It is the network device update role's url.
          returned: changed
          type: str
          sample: '<url>'

    version:
      description: NetworkDeviceBriefNIO's version.
      returned: changed
      type: str
      sample: '1.0'

"""

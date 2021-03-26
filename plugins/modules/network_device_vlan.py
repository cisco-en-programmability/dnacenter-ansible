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
module: network_device_vlan
short_description: Manage NetworkDeviceVlan objects of Devices
description:
- Returns Device Interface VLANs.
version_added: '1.0'
author: Rafael Campos (@racampos)
options:
  id:
    description:
    - Id path parameter.
    type: str
    required: True
  interface_type:
    description:
    - Vlan assocaited with sub-interface.
    type: str

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.network_device_vlan
# Reference by Internet resource
- name: NetworkDeviceVlan reference
  description: Complete reference of the NetworkDeviceVlan object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: NetworkDeviceVlan reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_device_interface_vlans
  cisco.dnac.network_device_vlan:
    state: query  # required
    id: SomeValue  # string, required
    interface_type: SomeValue  # string
  register: query_result
  """

RETURN = """
get_device_interface_vlans:
    description: Returns Device Interface VLANs.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body (list of objects).
      returned: always
      type: list
      contains:
        interfaceName:
          description: It is the network device vlan's interfaceName.
          returned: always
          type: str
          sample: '<interfacename>'
        ipAddress:
          description: It is the network device vlan's ipAddress.
          returned: always
          type: str
          sample: '<ipaddress>'
        mask:
          description: It is the network device vlan's mask.
          returned: always
          type: int
          sample: 0
        networkAddress:
          description: It is the network device vlan's networkAddress.
          returned: always
          type: str
          sample: '<networkaddress>'
        numberOfIPs:
          description: It is the network device vlan's numberOfIPs.
          returned: always
          type: int
          sample: 0
        prefix:
          description: It is the network device vlan's prefix.
          returned: always
          type: str
          sample: '<prefix>'
        vlanNumber:
          description: It is the network device vlan's vlanNumber.
          returned: always
          type: int
          sample: 0
        vlanType:
          description: It is the network device vlan's vlanType.
          returned: always
          type: str
          sample: '<vlantype>'

    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

"""

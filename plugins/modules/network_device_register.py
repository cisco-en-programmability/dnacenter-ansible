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
module: network_device_register
short_description: Manage NetworkDeviceRegister objects of Devices
description:
- Registers a device for WSA notification.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  macaddress:
    description:
    - Mac addres of the device.
    type: str
  serial_number:
    description:
    - Serial number of the device.
    type: str

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.network_device_register
# Reference by Internet resource
- name: NetworkDeviceRegister reference
  description: Complete reference of the NetworkDeviceRegister object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: NetworkDeviceRegister reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: register_device_for_wsa
  cisco.dnac.network_device_register:
    state: query  # required
    macaddress: SomeValue  # string
    serial_number: SomeValue  # string
  register: query_result
  
"""

RETURN = """
register_device_for_wsa:
    description: Registers a device for WSA notification.
    returned: always
    type: dict
    contains:
    response:
      description: Response, property of the response body.
      returned: always
      type: dict
      contains:
        macAddress:
          description: It is the network device register's macAddress.
          returned: always
          type: str
          sample: '<macaddress>'
        modelNumber:
          description: It is the network device register's modelNumber.
          returned: always
          type: str
          sample: '<modelnumber>'
        name:
          description: It is the network device register's name.
          returned: always
          type: str
          sample: '<name>'
        serialNumber:
          description: It is the network device register's serialNumber.
          returned: always
          type: str
          sample: '<serialnumber>'
        tenantId:
          description: It is the network device register's tenantId.
          returned: always
          type: str
          sample: '<tenantid>'

    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

"""

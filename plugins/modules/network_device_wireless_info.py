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
module: network_device_wireless_info
short_description: Manage NetworkDeviceWirelessInfo objects of Devices
description:
- Returns the wireless lan controller info with given device ID.
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
- module: cisco.dnac.plugins.module_utils.definitions.network_device_wireless_info
# Reference by Internet resource
- name: NetworkDeviceWirelessInfo reference
  description: Complete reference of the NetworkDeviceWirelessInfo object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: NetworkDeviceWirelessInfo reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_wireless_lan_controller_details_by_id
  cisco.dnac.network_device_wireless_info:
    state: query  # required
    id: SomeValue  # string, required
  register: query_result
  
"""

RETURN = """
get_wireless_lan_controller_details_by_id:
    description: Returns the wireless lan controller info with given device ID.
    returned: always
    type: dict
    contains:
      response:
      description: Response, property of the response body.
      returned: always
      type: dict
      contains:
        adminEnabledPorts:
          description: It is the network device wireless info's adminEnabledPorts.
          returned: always
          type: list
        apGroupName:
          description: It is the network device wireless info's apGroupName.
          returned: always
          type: str
          sample: '<apgroupname>'
        deviceId:
          description: It is the network device wireless info's deviceId.
          returned: always
          type: str
          sample: '<deviceid>'
        ethMacAddress:
          description: It is the network device wireless info's ethMacAddress.
          returned: always
          type: str
          sample: '<ethmacaddress>'
        flexGroupName:
          description: It is the network device wireless info's flexGroupName.
          returned: always
          type: str
          sample: '<flexgroupname>'
        id:
          description: It is the network device wireless info's id.
          returned: always
          type: str
          sample: '478012'
        instanceTenantId:
          description: It is the network device wireless info's instanceTenantId.
          returned: always
          type: str
          sample: '<instancetenantid>'
        instanceUuid:
          description: It is the network device wireless info's instanceUuid.
          returned: always
          type: str
          sample: '<instanceuuid>'
        lagModeEnabled:
          description: It is the network device wireless info's lagModeEnabled.
          returned: always
          type: bool
          sample: false
        netconfEnabled:
          description: It is the network device wireless info's netconfEnabled.
          returned: always
          type: bool
          sample: false
        wirelessLicenseInfo:
          description: It is the network device wireless info's wirelessLicenseInfo.
          returned: always
          type: str
          sample: '<wirelesslicenseinfo>'
        wirelessPackageInstalled:
          description: It is the network device wireless info's wirelessPackageInstalled.
          returned: always
          type: bool
          sample: false

    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

"""

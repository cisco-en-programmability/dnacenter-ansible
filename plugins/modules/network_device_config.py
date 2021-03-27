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
module: network_device_config
short_description: Manage NetworkDeviceConfig objects of Devices
description:
- Returns the config for all devices.
- Returns the count of device configs.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  count:
    description:
    - If true gets the number of objects.
    type: bool
    required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.network_device_config
# Reference by Internet resource
- name: NetworkDeviceConfig reference
  description: Complete reference of the NetworkDeviceConfig object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: NetworkDeviceConfig reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_device_config_for_all_devices
  cisco.dnac.network_device_config:
    state: query  # required

  register: query_result
  
- name: get_device_config_count
  cisco.dnac.network_device_config:
    state: query  # required
    count: True  # boolean, required
  register: query_result
  
"""

RETURN = """
get_device_config_for_all_devices:
    description: Returns the config for all devices.
    returned: always
    type: dict
    contains:
      response:
      description: Response, property of the response body (list of objects).
      returned: always
      type: list
      contains:
        attributeInfo:
          description: It is the network device config's attributeInfo.
          returned: always
          type: dict
        cdpNeighbors:
          description: It is the network device config's cdpNeighbors.
          returned: always
          type: str
          sample: '<cdpneighbors>'
        healthMonitor:
          description: It is the network device config's healthMonitor.
          returned: always
          type: str
          sample: '<healthmonitor>'
        id:
          description: It is the network device config's id.
          returned: always
          type: str
          sample: '478012'
        intfDescription:
          description: It is the network device config's intfDescription.
          returned: always
          type: str
          sample: '<intfdescription>'
        inventory:
          description: It is the network device config's inventory.
          returned: always
          type: str
          sample: '<inventory>'
        ipIntfBrief:
          description: It is the network device config's ipIntfBrief.
          returned: always
          type: str
          sample: '<ipintfbrief>'
        macAddressTable:
          description: It is the network device config's macAddressTable.
          returned: always
          type: str
          sample: '<macaddresstable>'
        runningConfig:
          description: It is the network device config's runningConfig.
          returned: always
          type: str
          sample: '<runningconfig>'
        snmp:
          description: It is the network device config's snmp.
          returned: always
          type: str
          sample: '<snmp>'
        version:
          description: It is the network device config's version.
          returned: always
          type: str
          sample: '1.0'

    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

get_device_config_count:
    description: Returns the count of device configs.
    returned: always
    type: dict
    contains:
      response:
      description: Response, property of the response body.
      returned: always
      type: int
      sample: 0
    version:
      description: Version, property of the response body.
      returned: always
      type: str
      sample: '1.0'

"""

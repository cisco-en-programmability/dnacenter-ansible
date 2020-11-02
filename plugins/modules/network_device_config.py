#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, first last <email>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    'metadata_version': '0.0.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = r'''
---
module: network_device_config
short_description: Manage NetworkDeviceConfig objects of Devices
description:
- Returns the config for all devices.
- Returns the count of device configs.
version_added: '1.0'
author: first last (@GitHubID)
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
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: Returns the config for all devices.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                attributeInfo:
                    description: It is the network device config's attributeInfo.
                    returned: success,changed,always
                    type: dict
                cdpNeighbors:
                    description: It is the network device config's cdpNeighbors.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                healthMonitor:
                    description: It is the network device config's healthMonitor.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                id:
                    description: It is the network device config's id.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                intfDescription:
                    description: It is the network device config's intfDescription.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                inventory:
                    description: It is the network device config's inventory.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                ipIntfBrief:
                    description: It is the network device config's ipIntfBrief.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                macAddressTable:
                    description: It is the network device config's macAddressTable.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                runningConfig:
                    description: It is the network device config's runningConfig.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                snmp:
                    description: It is the network device config's snmp.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                version:
                    description: It is the network device config's version.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_1:
    description: Returns the count of device configs.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body.
            returned: success,changed,always
            type: int
            sample: 0
        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ModuleDefinition, DNACModule, dnac_argument_spec
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.network_device_config import module_definition


def main():

    moddef = ModuleDefinition(module_definition)

    argument_spec = dnac_argument_spec()
    argument_spec.update(moddef.get_argument_spec_dict())

    required_if = moddef.get_required_if_list()
    
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=False,
        required_if=required_if
    )

    dnac = DNACModule(module, moddef)

    state = module.params.get("state")

    if state == "query":
        dnac.exec("get")

    dnac.exit_json()


if __name__ == "__main__":
    main()
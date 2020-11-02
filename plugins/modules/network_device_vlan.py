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
module: network_device_vlan
short_description: Manage NetworkDeviceVlan objects of Devices
description:
- Returns Device Interface VLANs.
version_added: '1.0'
author: first last (@GitHubID)
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
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: Returns Device Interface VLANs.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                interfaceName:
                    description: It is the network device vlan's interfaceName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                ipAddress:
                    description: It is the network device vlan's ipAddress.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                mask:
                    description: It is the network device vlan's mask.
                    returned: success,changed,always
                    type: int
                    sample: 0
                networkAddress:
                    description: It is the network device vlan's networkAddress.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                numberOfIPs:
                    description: It is the network device vlan's numberOfIPs.
                    returned: success,changed,always
                    type: int
                    sample: 0
                prefix:
                    description: It is the network device vlan's prefix.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                vlanNumber:
                    description: It is the network device vlan's vlanNumber.
                    returned: success,changed,always
                    type: int
                    sample: 0
                vlanType:
                    description: It is the network device vlan's vlanType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ModuleDefinition, DNACModule, dnac_argument_spec
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.network_device_vlan import module_definition


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
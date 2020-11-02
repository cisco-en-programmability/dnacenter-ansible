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
module: pnp_device_unclaim
short_description: Manage PnpDeviceUnclaim objects of DeviceOnboardingPnp
description:
- Un-Claims one of more devices with specified workflow.
version_added: '1.0'
author: first last (@GitHubID)
options:
    device_id_list:
        description:
        - UnclaimRequest's deviceIdList (list of strings).
        type: list

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.pnp_device_unclaim
# Reference by Internet resource
- name: PnpDeviceUnclaim reference
  description: Complete reference of the PnpDeviceUnclaim object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: PnpDeviceUnclaim reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: Un-Claims one of more devices with specified workflow.
    returned: success,changed,always
    type: dict
    contains:
        jsonArrayResponse:
            description: UnclaimRequest's Json Array Response (list of any objects).
            returned: success,changed,always
            type: list
        jsonResponse:
            description: UnclaimRequest's Json Response.
            returned: success,changed,always
            type: dict
        message:
            description: UnclaimRequest's Message.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        statusCode:
            description: UnclaimRequest's statusCode.
            returned: success,changed,always
            type: int
            sample: 0

'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ModuleDefinition, DNACModule, dnac_argument_spec
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.pnp_device_unclaim import module_definition


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

    if state == "create":
        dnac.exec("post")

    dnac.exit_json()


if __name__ == "__main__":
    main()
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
module: pnp_device_reset
short_description: Manage PnpDeviceReset objects of DeviceOnboardingPnp
description:
- Recovers a device from a Workflow Execution Error state.
version_added: '1.0'
author: first last (@GitHubID)
options:
    device_reset_list:
        description:
        - ResetRequest's deviceResetList (list of objects).
        type: list
        elements: dict
        suboptions:
            configList:
                description:
                - It is the pnp device reset's configList.
                type: list
                elements: dict
                suboptions:
                    configId:
                        description:
                        - It is the pnp device reset's configId.
                        type: str
                    configParameters:
                        description:
                        - It is the pnp device reset's configParameters.
                        type: list
                        elements: dict
                        suboptions:
                            key:
                                description:
                                - It is the pnp device reset's key.
                                type: str
                            value:
                                description:
                                - It is the pnp device reset's value.
                                type: str


            deviceId:
                description:
                - It is the pnp device reset's deviceId.
                type: str
            licenseLevel:
                description:
                - It is the pnp device reset's licenseLevel.
                type: str
            licenseType:
                description:
                - It is the pnp device reset's licenseType.
                type: str
            topOfStackSerialNumber:
                description:
                - It is the pnp device reset's topOfStackSerialNumber.
                type: str

    project_id:
        description:
        - ResetRequest's projectId.
        type: str
    workflow_id:
        description:
        - ResetRequest's workflowId.
        type: str

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.pnp_device_reset
# Reference by Internet resource
- name: PnpDeviceReset reference
  description: Complete reference of the PnpDeviceReset object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: PnpDeviceReset reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: Recovers a device from a Workflow Execution Error state.
    returned: success,changed,always
    type: dict
    contains:
        jsonArrayResponse:
            description: ResetRequest's Json Array Response (list of any objects).
            returned: success,changed,always
            type: list
        jsonResponse:
            description: ResetRequest's Json Response.
            returned: success,changed,always
            type: dict
        message:
            description: ResetRequest's Message.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        statusCode:
            description: ResetRequest's statusCode.
            returned: success,changed,always
            type: int
            sample: 0

'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ModuleDefinition, DNACModule, dnac_argument_spec
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.pnp_device_reset import module_definition


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
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
module: pnp_device_claim
short_description: Manage PnpDeviceClaim objects of DeviceOnboardingPnp
description:
- Claims one of more devices with specified workflow.
version_added: '1.0'
author: first last (@GitHubID)
options:
    config_file_url:
        description:
        - ClaimDeviceRequest's configFileUrl.
        type: str
    config_id:
        description:
        - ClaimDeviceRequest's configId.
        type: str
    device_claim_list:
        description:
        - ClaimDeviceRequest's deviceClaimList (list of objects).
        type: list
        elements: dict
        suboptions:
            configList:
                description:
                - It is the pnp device claim's configList.
                type: list
                elements: dict
                suboptions:
                    configId:
                        description:
                        - It is the pnp device claim's configId.
                        type: str
                    configParameters:
                        description:
                        - It is the pnp device claim's configParameters.
                        type: list
                        elements: dict
                        suboptions:
                            key:
                                description:
                                - It is the pnp device claim's key.
                                type: str
                            value:
                                description:
                                - It is the pnp device claim's value.
                                type: str


            deviceId:
                description:
                - It is the pnp device claim's deviceId.
                type: str
            licenseLevel:
                description:
                - It is the pnp device claim's licenseLevel.
                type: str
            licenseType:
                description:
                - It is the pnp device claim's licenseType.
                type: str
            topOfStackSerialNumber:
                description:
                - It is the pnp device claim's topOfStackSerialNumber.
                type: str

    file_service_id:
        description:
        - ClaimDeviceRequest's fileServiceId.
        type: str
    image_id:
        description:
        - ClaimDeviceRequest's imageId.
        type: str
    image_url:
        description:
        - ClaimDeviceRequest's imageUrl.
        type: str
    populate_inventory:
        description:
        - ClaimDeviceRequest's populateInventory.
        type: bool
    project_id:
        description:
        - ClaimDeviceRequest's projectId.
        type: str
    workflow_id:
        description:
        - ClaimDeviceRequest's workflowId.
        type: str

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.pnp_device_claim
# Reference by Internet resource
- name: PnpDeviceClaim reference
  description: Complete reference of the PnpDeviceClaim object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: PnpDeviceClaim reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: Claims one of more devices with specified workflow.
    returned: success,changed,always
    type: dict
    contains:
        jsonArrayResponse:
            description: ClaimDeviceRequest's Json Array Response (list of any objects).
            returned: success,changed,always
            type: list
        jsonResponse:
            description: ClaimDeviceRequest's Json Response.
            returned: success,changed,always
            type: dict
        message:
            description: ClaimDeviceRequest's Message.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        statusCode:
            description: ClaimDeviceRequest's statusCode.
            returned: success,changed,always
            type: int
            sample: 0

'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ModuleDefinition, DNACModule, dnac_argument_spec
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.pnp_device_claim import module_definition


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
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
module: device_replacement_workflow
short_description: Manage DeviceReplacementWorkflow objects of DeviceReplacement
description:
- API to trigger RMA workflow that will replace faulty device with replacement device with same configuration and images.
version_added: '1.0'
author: first last (@GitHubID)
options:
    faultyDeviceSerialNumber:
        description:
        - DeviceReplacementWorkflowDTO's faultyDeviceSerialNumber.
        type: str
        required: True
    replacementDeviceSerialNumber:
        description:
        - DeviceReplacementWorkflowDTO's replacementDeviceSerialNumber.
        type: str
        required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.device_replacement_workflow
# Reference by Internet resource
- name: DeviceReplacementWorkflow reference
  description: Complete reference of the DeviceReplacementWorkflow object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: DeviceReplacementWorkflow reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: API to trigger RMA workflow that will replace faulty device with replacement device with same configuration and images.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: DeviceReplacementWorkflowDTO's response.
            returned: success,changed,always
            type: dict
            contains:
                taskId:
                    description: It is the device replacement workflow's taskId.
                    returned: success,changed,always
                    type: dict
                url:
                    description: It is the device replacement workflow's url.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        version:
            description: DeviceReplacementWorkflowDTO's version.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ModuleDefinition, DNACModule, dnac_argument_spec
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.device_replacement_workflow import module_definition


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
        dnac.disable_validation()
        dnac.exec("post")

    dnac.exit_json()


if __name__ == "__main__":
    main()
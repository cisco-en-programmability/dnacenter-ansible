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
module: trigger_image_distribution
short_description: Manage TriggerImageDistribution objects of SoftwareImageManagementSwim
description:
- Distributes a software image on a given device. Software image must be imported successfully into DNA Center before it can be distributed.
version_added: '1.0'
author: first last (@GitHubID)
options:
    payload:
        description:
        - An object to send in the Request body.
        type: list
        required: True
        elements: dict
        suboptions:
            deviceUuid:
                description:
                - It is the trigger image distribution's deviceUuid.
                type: str
            imageUuid:
                description:
                - It is the trigger image distribution's imageUuid.
                type: str


requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.trigger_image_distribution
# Reference by Internet resource
- name: TriggerImageDistribution reference
  description: Complete reference of the TriggerImageDistribution object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: TriggerImageDistribution reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: Distributes a software image on a given device. Software image must be imported successfully into DNA Center before it can be distributed.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: DistributeDTO's response.
            returned: success,changed,always
            type: dict
            contains:
                taskId:
                    description: It is the trigger image distribution's taskId.
                    returned: success,changed,always
                    type: dict
                url:
                    description: It is the trigger image distribution's url.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        version:
            description: DistributeDTO's version.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ModuleDefinition, DNACModule, dnac_argument_spec
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.trigger_image_distribution import module_definition


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
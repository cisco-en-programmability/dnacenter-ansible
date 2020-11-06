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
module: network_device_poller_read_request
short_description: Manage NetworkDevicePollerReadRequest objects of CommandRunner
description:
- Submit request for read-only CLIs.
version_added: '1.0'
author: first last (@GitHubID)
options:
    commands:
        description:
        - CommandRunnerDTO's commands (list of strings).
        type: list
        required: True
    description:
        description:
        - CommandRunnerDTO's description.
        type: str
    deviceUuids:
        description:
        - CommandRunnerDTO's deviceUuids (list of strings).
        type: list
        required: True
    name:
        description:
        - CommandRunnerDTO's name.
        type: str
    timeout:
        description:
        - CommandRunnerDTO's timeout.
        type: int

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.network_device_poller_read_request
# Reference by Internet resource
- name: NetworkDevicePollerReadRequest reference
  description: Complete reference of the NetworkDevicePollerReadRequest object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: NetworkDevicePollerReadRequest reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: Submit request for read-only CLIs.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: CommandRunnerDTO's response.
            returned: success,changed,always
            type: dict
            contains:
                taskId:
                    description: It is the network device poller read request's taskId.
                    returned: success,changed,always
                    type: dict
                url:
                    description: It is the network device poller read request's url.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        version:
            description: CommandRunnerDTO's version.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ModuleDefinition, DNACModule, dnac_argument_spec
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.network_device_poller_read_request import module_definition


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
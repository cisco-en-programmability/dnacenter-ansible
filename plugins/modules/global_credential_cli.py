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
module: global_credential_cli
short_description: Manage GlobalCredentialCli objects of Discovery
description:
- Adds global CLI credential.
- Updates global CLI credentials.
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
            comments:
                description:
                - It is the global credential cli's comments.
                type: str
            credentialType:
                description:
                - It is the global credential cli's credentialType.
                type: str
            description:
                description:
                - It is the global credential cli's description.
                type: str
            enablePassword:
                description:
                - It is the global credential cli's enablePassword.
                type: str
                required: True
            id:
                description:
                - It is the global credential cli's id.
                type: str
            instanceTenantId:
                description:
                - It is the global credential cli's instanceTenantId.
                type: str
            instanceUuid:
                description:
                - It is the global credential cli's instanceUuid.
                type: str
            password:
                description:
                - It is the global credential cli's password.
                type: str
                required: True
            username:
                description:
                - It is the global credential cli's username.
                type: str
                required: True

    comments:
        description:
        - CLICredentialDTO's comments.
        type: str
    credentialType:
        description:
        - CLICredentialDTO's credentialType.
        - Available values are 'GLOBAL' and 'APP'.
        type: str
    description:
        description:
        - CLICredentialDTO's description.
        type: str
    enablePassword:
        description:
        - CLICredentialDTO's enablePassword.
        type: str
        required: True
    id:
        description:
        - CLICredentialDTO's id.
        type: str
    instanceTenantId:
        description:
        - CLICredentialDTO's instanceTenantId.
        type: str
    instanceUuid:
        description:
        - CLICredentialDTO's instanceUuid.
        type: str
    password:
        description:
        - CLICredentialDTO's password.
        type: str
        required: True
    username:
        description:
        - CLICredentialDTO's username.
        type: str
        required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.global_credential_cli
# Reference by Internet resource
- name: GlobalCredentialCli reference
  description: Complete reference of the GlobalCredentialCli object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: GlobalCredentialCli reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: Adds global CLI credential.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: CLICredentialDTO's response.
            returned: success,changed,always
            type: dict
            contains:
                taskId:
                    description: It is the global credential cli's taskId.
                    returned: success,changed,always
                    type: dict
                url:
                    description: It is the global credential cli's url.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        version:
            description: CLICredentialDTO's version.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_1:
    description: Updates global CLI credentials.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: CLICredentialDTO's response.
            returned: success,changed,always
            type: dict
            contains:
                taskId:
                    description: It is the global credential cli's taskId.
                    returned: success,changed,always
                    type: dict
                url:
                    description: It is the global credential cli's url.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        version:
            description: CLICredentialDTO's version.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ModuleDefinition, DNACModule, dnac_argument_spec
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.global_credential_cli import module_definition


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

    elif state == "update":
        dnac.disable_validation()
        dnac.exec("put")

    dnac.exit_json()


if __name__ == "__main__":
    main()
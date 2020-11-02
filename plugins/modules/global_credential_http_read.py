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
module: global_credential_http_read
short_description: Manage GlobalCredentialHttpRead objects of Discovery
description:
- Adds HTTP read credentials.
- Updates global HTTP Read credential.
version_added: '1.0'
author: first last (@GitHubID)
options:
    payload:
        description:
        - A JSON serializable Python object to send in the body of the Request.
        type: list
        required: True
        elements: dict
        suboptions:
            comments:
                description:
                - It is the global credential http read's comments.
                type: str
            credentialType:
                description:
                - It is the global credential http read's credentialType.
                type: str
            description:
                description:
                - It is the global credential http read's description.
                type: str
            id:
                description:
                - It is the global credential http read's id.
                type: str
            instanceTenantId:
                description:
                - It is the global credential http read's instanceTenantId.
                type: str
            instanceUuid:
                description:
                - It is the global credential http read's instanceUuid.
                type: str
            password:
                description:
                - It is the global credential http read's password.
                type: str
                required: True
            port:
                description:
                - It is the global credential http read's port.
                type: int
                required: True
            secure:
                description:
                - It is the global credential http read's secure.
                type: bool
            username:
                description:
                - It is the global credential http read's username.
                type: str
                required: True

    comments:
        description:
        - HTTPReadCredentialDTO's comments.
        type: str
    credential_type:
        description:
        - HTTPReadCredentialDTO's credentialType.
        type: str
        choices: ['GLOBAL', 'APP']
    description:
        description:
        - HTTPReadCredentialDTO's description.
        type: str
    id:
        description:
        - HTTPReadCredentialDTO's id.
        type: str
    instance_tenant_id:
        description:
        - HTTPReadCredentialDTO's instanceTenantId.
        type: str
    instance_uuid:
        description:
        - HTTPReadCredentialDTO's instanceUuid.
        type: str
    password:
        description:
        - HTTPReadCredentialDTO's password.
        type: str
        required: True
    port:
        description:
        - HTTPReadCredentialDTO's port.
        type: int
        required: True
    secure:
        description:
        - HTTPReadCredentialDTO's secure.
        type: bool
    username:
        description:
        - HTTPReadCredentialDTO's username.
        type: str
        required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.global_credential_http_read
# Reference by Internet resource
- name: GlobalCredentialHttpRead reference
  description: Complete reference of the GlobalCredentialHttpRead object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: GlobalCredentialHttpRead reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: Adds HTTP read credentials.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: HTTPReadCredentialDTO's response.
            returned: success,changed,always
            type: dict
            contains:
                taskId:
                    description: It is the global credential http read's taskId.
                    returned: success,changed,always
                    type: dict
                url:
                    description: It is the global credential http read's url.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        version:
            description: HTTPReadCredentialDTO's version.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_1:
    description: Updates global HTTP Read credential.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: HTTPReadCredentialDTO's response.
            returned: success,changed,always
            type: dict
            contains:
                taskId:
                    description: It is the global credential http read's taskId.
                    returned: success,changed,always
                    type: dict
                url:
                    description: It is the global credential http read's url.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'

        version:
            description: HTTPReadCredentialDTO's version.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ModuleDefinition, DNACModule, dnac_argument_spec
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.global_credential_http_read import module_definition


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

    elif state == "update":
        dnac.exec("put")

    dnac.exit_json()


if __name__ == "__main__":
    main()
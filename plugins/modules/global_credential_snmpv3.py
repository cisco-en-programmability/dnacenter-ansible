#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, first last <email>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    "metadata_version": "0.0.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
---
module: global_credential_snmpv3
short_description: Manage GlobalCredentialSnmpv3 objects of Discovery
description:
- Adds global SNMPv3 credentials.
- Updates global SNMPv3 credential.
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
            authPassword:
                description:
                - It is the global credential snmpv3's authPassword.
                type: str
            authType:
                description:
                - It is the global credential snmpv3's authType.
                type: str
            comments:
                description:
                - It is the global credential snmpv3's comments.
                type: str
            credentialType:
                description:
                - It is the global credential snmpv3's credentialType.
                type: str
            description:
                description:
                - It is the global credential snmpv3's description.
                type: str
            id:
                description:
                - It is the global credential snmpv3's id.
                type: str
            instanceTenantId:
                description:
                - It is the global credential snmpv3's instanceTenantId.
                type: str
            instanceUuid:
                description:
                - It is the global credential snmpv3's instanceUuid.
                type: str
            privacyPassword:
                description:
                - It is the global credential snmpv3's privacyPassword.
                type: str
            privacyType:
                description:
                - It is the global credential snmpv3's privacyType.
                type: str
            snmpMode:
                description:
                - It is the global credential snmpv3's snmpMode.
                type: str
                required: True
            username:
                description:
                - It is the global credential snmpv3's username.
                type: str
                required: True

    authPassword:
        description:
        - SNMPv3CredentialDTO's authPassword.
        type: str
    authType:
        description:
        - SNMPv3CredentialDTO's authType.
        - Available values are 'SHA' and 'MD5'.
        type: str
    comments:
        description:
        - SNMPv3CredentialDTO's comments.
        type: str
    credentialType:
        description:
        - SNMPv3CredentialDTO's credentialType.
        - Available values are 'GLOBAL' and 'APP'.
        type: str
    description:
        description:
        - SNMPv3CredentialDTO's description.
        type: str
    id:
        description:
        - SNMPv3CredentialDTO's id.
        type: str
    instanceTenantId:
        description:
        - SNMPv3CredentialDTO's instanceTenantId.
        type: str
    instanceUuid:
        description:
        - SNMPv3CredentialDTO's instanceUuid.
        type: str
    privacyPassword:
        description:
        - SNMPv3CredentialDTO's privacyPassword.
        type: str
    privacyType:
        description:
        - SNMPv3CredentialDTO's privacyType.
        - Available values are 'DES' and 'AES128'.
        type: str
    snmpMode:
        description:
        - SNMPv3CredentialDTO's snmpMode.
        - Available values are 'AUTHPRIV', 'AUTHNOPRIV' and 'NOAUTHNOPRIV'.
        type: str
        required: True
    username:
        description:
        - SNMPv3CredentialDTO's username.
        type: str
        required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.global_credential_snmpv3
# Reference by Internet resource
- name: GlobalCredentialSnmpv3 reference
  description: Complete reference of the GlobalCredentialSnmpv3 object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: GlobalCredentialSnmpv3 reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
"""

RETURN = r"""
data_0:
    description: Adds global SNMPv3 credentials.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: SNMPv3CredentialDTO's response.
            returned: success,changed,always
            type: dict
            contains:
                taskId:
                    description: It is the global credential snmpv3's taskId.
                    returned: success,changed,always
                    type: dict
                url:
                    description: It is the global credential snmpv3's url.
                    returned: success,changed,always
                    type: str
                    sample: '<url>'

        version:
            description: SNMPv3CredentialDTO's version.
            returned: success,changed,always
            type: str
            sample: '1.0'

data_1:
    description: Updates global SNMPv3 credential.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: SNMPv3CredentialDTO's response.
            returned: success,changed,always
            type: dict
            contains:
                taskId:
                    description: It is the global credential snmpv3's taskId.
                    returned: success,changed,always
                    type: dict
                url:
                    description: It is the global credential snmpv3's url.
                    returned: success,changed,always
                    type: str
                    sample: '<url>'

        version:
            description: SNMPv3CredentialDTO's version.
            returned: success,changed,always
            type: str
            sample: '1.0'

"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    ModuleDefinition,
    DNACModule,
    dnac_argument_spec,
)
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.global_credential_snmpv3 import (
    module_definition,
)


def main():

    moddef = ModuleDefinition(module_definition)

    argument_spec = dnac_argument_spec()
    argument_spec.update(moddef.get_argument_spec_dict())

    required_if = moddef.get_required_if_list()

    module = AnsibleModule(
        argument_spec=argument_spec, supports_check_mode=False, required_if=required_if
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

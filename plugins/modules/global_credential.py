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
module: global_credential
short_description: Manage GlobalCredential objects of Discovery
description:
- Returns global credential for the given credential sub type.
- Deletes global credential for the given ID.
- Update global credential for network devices in site(s).
- Returns the credential sub type for the given Id.
version_added: '1.0'
author: first last (@GitHubID)
options:
    credential_sub_type:
        description:
        - Credential type as CLI / SNMPV2_READ_COMMUNITY / SNMPV2_WRITE_COMMUNITY / SNMPV3 / HTTP_WRITE / HTTP_READ / NETCONF.
        type: str
    order:
        description:
        - Order query parameter.
        type: str
    sort_by:
        description:
        - SortBy query parameter.
        type: str
    global_credential_id:
        description:
        - ID of global-credential.
        type: str
        required: True
    siteUuids:
        description:
        - SitesInfoDTO's siteUuids (list of strings).
        type: list
    id:
        description:
        - Global Credential ID.
        type: str
        required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.global_credential
# Reference by Internet resource
- name: GlobalCredential reference
  description: Complete reference of the GlobalCredential object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: GlobalCredential reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
"""

RETURN = r"""
data_0:
    description: Returns global credential for the given credential sub type.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body (list of objects).
            returned: success,changed,always
            type: list
            contains:
                comments:
                    description: It is the global credential's comments.
                    returned: success,changed,always
                    type: str
                    sample: '<comments>'
                credentialType:
                    description: It is the global credential's credentialType.
                    returned: success,changed,always
                    type: str
                    sample: '<credentialtype>'
                description:
                    description: It is the global credential's description.
                    returned: success,changed,always
                    type: str
                    sample: '<description>'
                id:
                    description: It is the global credential's id.
                    returned: success,changed,always
                    type: str
                    sample: '478012'
                instanceTenantId:
                    description: It is the global credential's instanceTenantId.
                    returned: success,changed,always
                    type: str
                    sample: '<instancetenantid>'
                instanceUuid:
                    description: It is the global credential's instanceUuid.
                    returned: success,changed,always
                    type: str
                    sample: '<instanceuuid>'

        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: '1.0'

data_1:
    description: Deletes global credential for the given ID.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                taskId:
                    description: It is the global credential's taskId.
                    returned: success,changed,always
                    type: dict
                url:
                    description: It is the global credential's url.
                    returned: success,changed,always
                    type: str
                    sample: '<url>'

        version:
            description: Version, property of the response body.
            returned: success,changed,always
            type: str
            sample: '1.0'

data_2:
    description: Update global credential for network devices in site(s).
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: SitesInfoDTO's response.
            returned: success,changed,always
            type: dict
            contains:
                taskId:
                    description: It is the global credential's taskId.
                    returned: success,changed,always
                    type: dict
                url:
                    description: It is the global credential's url.
                    returned: success,changed,always
                    type: str
                    sample: '<url>'

        version:
            description: SitesInfoDTO's version.
            returned: success,changed,always
            type: str
            sample: '1.0'

data_3:
    description: Returns the credential sub type for the given Id.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body.
            returned: success,changed,always
            type: str
            sample: '<response>'
        version:
            description: Version, property of the response body.
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
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.global_credential import (
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

    if state == "query":
        dnac.exec("get")

    elif state == "delete":
        dnac.exec("delete")

    elif state == "update":
        dnac.disable_validation()
        dnac.exec("put")

    dnac.exit_json()


if __name__ == "__main__":
    main()

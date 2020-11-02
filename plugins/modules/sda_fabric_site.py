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
module: sda_fabric_site
short_description: Manage SdaFabricSite objects of Sda
description:
- Delete Site from SDA Fabric.
- Get Site info from SDA Fabric.
- Add Site in SDA Fabric.
version_added: '1.0'
author: first last (@GitHubID)
options:
    site_name_hierarchy:
        description:
        - Site Name Hierarchy.
        type: str
    site_name_hierarchy:
        description:
        - Site Name Hierarchy.
        type: str
    payload:
        description:
        - A JSON serializable Python object to send in the body of the Request.
        type: list
        required: True
        elements: dict
        suboptions:
            fabricName:
                description:
                - It is the sda fabric site's fabricName.
                type: str
            siteNameHierarchy:
                description:
                - It is the sda fabric site's siteNameHierarchy.
                type: str


requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.sda_fabric_site
# Reference by Internet resource
- name: SdaFabricSite reference
  description: Complete reference of the SdaFabricSite object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: SdaFabricSite reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: Delete Site from SDA Fabric.
    returned: success,changed,always
    type: dict
    contains:
        status:
            description: Status, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        description:
            description: Description, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        executionStatusUrl:
            description: Execution Status Url, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_1:
    description: Get Site info from SDA Fabric.
    returned: success,changed,always
    type: dict
    contains:
        status:
            description: Status, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        description:
            description: Description, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        executionStatusUrl:
            description: Execution Status Url, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

data_2:
    description: Add Site in SDA Fabric.
    returned: success,changed,always
    type: dict
    contains:
        status:
            description: Status, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        description:
            description: Description, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'
        executionStatusUrl:
            description: Execution Status Url, property of the response body.
            returned: success,changed,always
            type: str
            sample: 'sample_string'

'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ModuleDefinition, DNACModule, dnac_argument_spec
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.sda_fabric_site import module_definition


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

    if state == "query":
        dnac.exec("get")

    elif state == "delete":
        dnac.exec("delete")

    elif state == "create":
        dnac.exec("post")

    dnac.exit_json()


if __name__ == "__main__":
    main()